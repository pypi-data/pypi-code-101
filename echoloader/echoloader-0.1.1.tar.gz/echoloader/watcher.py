import argparse
import base64
import json
import logging
import math
import os
import re
import sys
import threading
import time
from getpass import getpass
from io import BytesIO
from multiprocessing.dummy import Pool
from pathlib import Path
from time import sleep

import cv2
import numpy as np
import pydicom
import requests
from pycognito import Cognito
from pydicom import uid
from pydicom._storage_sopclass_uids import UltrasoundMultiFrameImageStorage, UltrasoundImageStorage
from pydicom.encaps import encapsulate
from pydicom.pixel_data_handlers import apply_color_lut
from pynetdicom import (
    AE, evt, ALL_TRANSFER_SYNTAXES
)
from pynetdicom.sop_class import _VERIFICATION_CLASSES
from tqdm import tqdm
from watchdog.events import FileCreatedEvent, FileMovedEvent, FileModifiedEvent
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

logger = logging.getLogger('echolog')
OS_VAR_PREFIX = 'US2_'


class AWS:
    def __init__(self, env):
        self.app_url = f'https://{"" if env and env == "production" else env + "-"}app.us2.ai'
        self.service_url = re.sub(r'\bapp\b', 'services', self.app_url)
        self.presign_url = f'{self.service_url}/presign'
        self.app_config = requests.get(f'{self.app_url}/en/assets/config.json').json()
        self.client_id = self.app_config['awsConfig']['aws_user_pools_web_client_id']
        self.user_pool_id = self.app_config['awsConfig']['aws_user_pools_id']


class Us2CognitoException(Exception):
    pass


class Refresher(threading.Thread):
    def __init__(self, cognito, pw, delay=55 * 60):
        super().__init__()
        self.cognito = cognito
        self.pw = pw
        self.delay = delay
        self._kill = threading.Event()

    def run(self):
        while True:
            is_killed = self._kill.wait(self.delay)
            if is_killed:
                break
            self.cognito.authenticate(password=self.pw)

    def kill(self):
        self._kill.set()


class Us2Cognito(Cognito):
    def __init__(self, args, username, password):
        super().__init__(args.env.user_pool_id, args.env.client_id, username=username)
        self.authenticate(password=password)
        self.refresher = Refresher(self, password)
        self.refresher.start()

    @classmethod
    def get_payload(cls, token):
        payload_text = token.split('.')[1]
        return json.loads(base64.b64decode(payload_text + '===').decode())

    def get_headers(self):
        return {"Authorization": f"Bearer {self.id_token}"}

    def get_cookies(self):
        return {".idToken": self.id_token}

    def groups(self, prefix="", suffix=""):
        payload = self.get_payload(self.id_token)
        return [s for s in payload.get('cognito:groups', []) if s.startswith(prefix) and s.endswith(suffix)]

    def customer(self):
        groups = self.groups('s3-')
        if not groups:
            raise Us2CognitoException('No access to any s3 bucket')
        return groups[0].split('-', 1)[1]

    def logout(self):
        self.refresher.kill()
        return super().logout()

    def stop(self):
        self.refresher.kill()

    def join(self):
        pass


def is_video(img=None, shape=None):
    shape = shape or (isinstance(img, np.ndarray) and img.shape)
    return shape and (len(shape) == 4 or (len(shape) == 3 and shape[-1] > 4))


def ybr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_YCR_CB2BGR)


def blank_top_bar(media, regions):
    video = is_video(media)
    image = np.mean(media, axis=0) if video else media
    new_image = np.mean(image[..., :3], axis=-1) if 3 <= image.shape[-1] <= 4 else image
    binary_image = (new_image > 2).astype('uint8')
    h = int(binary_image.shape[0] * 0.2)
    sum_pixel = np.sum(binary_image[:h, :], axis=1)
    top_bar = np.where(sum_pixel > (binary_image.shape[0] * 0.88))
    top_bar_bottom = 0
    if len(top_bar[0]) != 0:
        new_image[top_bar, :] = 0
        image[top_bar, :] = 0
        top_bar_bottom = top_bar[0][-1] + 1
    top_bar_bottom = max(top_bar_bottom, 40)
    mask = np.ones_like(media[0] if video else media)
    mask[:top_bar_bottom] = 0
    for region in regions:
        xo, xn = region.RegionLocationMinX0, region.RegionLocationMaxX1
        yo, yn = region.RegionLocationMinY0, region.RegionLocationMaxY1
        mask[yo:yn, xo:xn] = 1
    media *= mask


def parse_dicom_pixel(dicom):
    px = dicom.pixel_array
    pi = dicom.PhotometricInterpretation
    dicom.PhotometricInterpretation = 'RGB'
    if pi in ['YBR_FULL', 'YBR_FULL_422']:
        px = np.asarray([ybr_to_rgb(img) for img in px]) if is_video(px) else ybr_to_rgb(px)
    elif pi in ['PALETTE COLOR']:
        px = (apply_color_lut(px, dicom) // 255).astype('uint8')
    else:
        dicom.PhotometricInterpretation = pi
    blank_top_bar(px, getattr(dicom, "SequenceOfUltrasoundRegions", []))
    return px


def ensure_even(stream):
    # Very important for some viewers
    if len(stream) % 2:
        return stream + b"\x00"
    return stream


def person_data_callback(ds, e):
    if e.VR == "PN" or e.tag == (0x0010, 0x0030):
        del ds[e.tag]


def anonymize_dicom(ds):
    # Populate required values for file meta information
    ds.remove_private_tags()
    ds.walk(person_data_callback)
    media = parse_dicom_pixel(ds)
    video = is_video(media)
    ds.file_meta.TransferSyntaxUID = uid.JPEGExtended

    ds.is_little_endian = True
    ds.is_implicit_VR = False

    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7

    ds.Rows, ds.Columns, ds.SamplesPerPixel = media.shape[video:]
    if video:
        ds.StartTrim = 1
        ds.StopTrim = ds.NumberOfFrames = media.shape[0] if video else 1
        ds.CineRate = ds.RecommendedDisplayFrameRate = 63
        ds.FrameTime = 1000 / ds.CineRate
        ds.ActualFrameDuration = math.ceil(1000 / ds.CineRate)
        ds.PreferredPlaybackSequencing = 0
        ds.FrameDelay = 0
    ds.PhotometricInterpretation = "YBR_FULL"
    ds.PixelData = encapsulate([ensure_even(cv2.imencode('.jpg', img)[1].tobytes())
                                for img in (media if video else [media])])
    ds['PixelData'].is_undefined_length = True


def wait_file(path):
    path = Path(path)
    old = None
    cur = os.path.getsize(path)
    while old != cur or not cur:
        sleep(1)
        old, cur = cur, os.path.getsize(path)


class Handler(FileSystemEventHandler):
    def __init__(self, args):
        self.args = args
        self.pool = Pool(args.n)
        self.pbar = tqdm(total=0)
        self.closed = False

    def processing(self):
        return self.pbar.n < self.pbar.total

    def stop(self):
        self.closed = True
        self.pool.terminate()

    def join(self):
        self.pool.join()

    def upload(self, ds):
        content_type = 'application/dicom'
        customer = self.args.customer
        data = {
            'customer': customer,
            'trial': customer,
            'patient_id': ds.PatientID,
            'visit_id': ds.StudyID,
            'filename': f"{ds.SOPInstanceUID}.dcm",
            'content_type': content_type,
        }
        headers = self.args.cognito.get_headers()
        r = requests.post(self.args.env.presign_url, json=data, headers=headers)
        r.raise_for_status()
        url = r.json()
        buf = BytesIO()
        ds.save_as(buf)
        buf.seek(0)
        r = requests.put(url, data=buf.read(), headers={'Content-type': content_type})
        r.raise_for_status()

    def process(self, path=None, ds=None):
        self.pbar.disable = False
        if self.closed:
            return
        if path:
            path = Path(path)
            ds = pydicom.dcmread(path)
        anonymize_dicom(ds)
        dst = self.args.dst
        if dst:
            src = self.args.src
            rel = path.relative_to(src)
            out = (dst / rel).with_suffix(".dcm")
            if self.args.overwrite or not out.is_file():
                out.parent.mkdir(exist_ok=True, parents=True)
                ds.save_as(out)
        if hasattr(self.args, "cognito"):
            self.upload(ds)
        self.pbar.update(1)

    def handle_err(self, err):
        logger.error('Error during process call: %s', err)
        self.pbar.update(1)

    def handle(self, *vargs, **kwargs):
        self.pbar.total += 1
        self.pbar.refresh()
        self.pool.apply_async(self.process, vargs, kwargs, error_callback=self.handle_err)

    def on_any_event(self, event):
        logger.debug(f'got event {event}')
        if isinstance(event, (FileCreatedEvent, FileMovedEvent, FileModifiedEvent)):
            path = event.src_path
            wait_file(path)
            self.handle(path)


def handle_store(event, handler):
    """Handle EVT_C_STORE events."""
    handler.handle(ds=event.dataset)
    return 0x0000


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src", type=Path, help="The folder to anonymize")
    parser.add_argument(
        "--dst", help="The output folder for the anonymized DICOM, defaults to src folder suffixed with '_anonymized'")
    parser.add_argument(
        "--watch", action="store_true", help="Watch the src folder for changes")
    parser.add_argument(
        "--pacs", action="store_true", help="Starts PACS server")
    parser.add_argument(
        "--pacs-ae-title", default="Us2.ai", help="PACS AE Title, defaults to Us2.ai")
    parser.add_argument(
        "--pacs-port", default=11112, help="PACS port, defaults to 11112", type=int)
    parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite files in the output folder")
    parser.add_argument(
        "--n", help="Number of workers", type=int, default=4)
    parser.add_argument(
        "--upload", action='store_true', help="Will upload all anonymized imaging to Us2.ai cloud")
    parser.add_argument(
        "--env", type=AWS, help="The Us2.ai environment to use", default=AWS('production'))
    args = parser.parse_args(sys.argv[1:])
    if args.upload:
        args.cognito = Us2Cognito(
            args,
            os.environ.get(f"{OS_VAR_PREFIX}COGNITO_USERNAME") or input("username: "),
            os.environ.get(f"{OS_VAR_PREFIX}COGNITO_PASSWORD") or getpass("password: ")
        )
        args.customer = args.cognito.groups(prefix='s3-')[0][3:]
    handler = Handler(args)
    try:
        if args.src:
            src = args.src
            args.dst = Path(args.dst or src.parent / f"{src.stem}_anonymized")
            paths = [src] if src.is_file() else list(src.rglob("*"))
            args.n = len(paths)
            args.i = 0
            for path in paths:
                handler.handle(path)
            if args.watch:
                logger.warning(f"watching folder {os.path.abspath(src)}")
                src.mkdir(exist_ok=True, parents=True)
                observer = args.observer = Observer()
                observer.schedule(handler, src, recursive=True)
                observer.start()
        if args.pacs:
            logger.warning(f"Starting pacs server on 0.0.0.0:{args.pacs_port} with AE title {args.pacs_ae_title}")
            handlers = [(evt.EVT_C_STORE, handle_store, [handler])]
            ae = AE()
            ae.add_supported_context(str(UltrasoundMultiFrameImageStorage))
            ae.add_supported_context(str(UltrasoundImageStorage))
            ae.add_supported_context(_VERIFICATION_CLASSES['VerificationSOPClass'], ALL_TRANSFER_SYNTAXES)
            ae.start_server(('0.0.0.0', args.pacs_port), block=True, evt_handlers=handlers, ae_title=args.pacs_ae_title)
        while hasattr(args, 'observer') or handler.processing():
            time.sleep(1)
    except KeyboardInterrupt:
        logger.warning("Interrupted, finishing up jobs")
    finally:
        to_wait = [handler, getattr(args, 'observer', None), getattr(args, 'cognito', None)]
        to_wait = [e for e in to_wait if e]
        for e in to_wait:
            e.stop()
        for e in to_wait:
            e.join()
