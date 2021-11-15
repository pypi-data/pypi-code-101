#Patent Pending

# Used to respond to events of text appearing on screen.
#    "apply_tesseract": False,

RECT_KEY = 'rect'
OCR_RECT_KEY = 'ocr_rect'
RECTS_KEY = 'rects'
ASSISTED_LABEL_RECT_KEY = 'assisted_label_rect'
THRESHOLD_KEY = 'threshold'
OCR_CONFIG_KEY = 'ocr_config'
LABELS_TO_TRACK_KEY = 'labels_to_track'
OVERRIDE_RECTS_KEY = 'override_rects'
IGNORE_IF_TRIGGERS_KEY = 'ignore_if_triggers'
IGNORE_IF_LABELS_EXIST_KEY = 'ignore_if_labels_exists'
IGNORE_IF_REGEX_TRIGGERED_KEY = 'ignore_if_regex_triggered'
REQUIRED_REGEX_TRIGGERED_KEY = 'ignore_if_regex_triggered'
TRACKING_CONFIGURATIONS_KEY = 'tracking_configurations'

import os
import re
REJECT_DUPLICATE_MESSAGES = bool(int(os.environ.get('REJECT_DUPLICATE_MESSAGES', 1)))
SAVE_MESSAGE_FRAMES = bool(int(os.environ.get('SAVE_MESSAGE_FRAMES', 1)))
ACCEPTED_MESSAGE_DIR = './accepted_message_frames'
REJECTED_MESSAGE_DIR = './rejected_message_frames'
DRAW_FRAMES_DIR = 'draw_frames'

import uuid

import io
from PIL import Image
import redis

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)


class TextTracker():
    def __init__(self, config, pool, user_id, session_id):
        super().__init__(user_id, session_id, 'text_tracker')

        self.config = config
        self.futures = []
        self.pool = pool


        self.occurences  = {}
        self.assisted_occurences = {}
        self.ignored_occurences = {}
        self.processed_text = {}
        self.rejected_text = {}

        self.all_accepted_messages = []
        self.all_rejected_messages = []
        self.messages_in_order = []
        self.text_counts = {}

        # For local storage outside of redis
        self.stored_messages_for_local = []
        self.last_frame_mapping = {}


    def process_frame(self, frame_key, frame, label_and_boxes):
        self.save_frame_key(frame_key)

        labels_to_track = self.config[LABELS_TO_TRACK_KEY]
        # first pass is only for checking if frame exists or needs to be added.

        did_assist_in_detection = False
        assist_labels = []

        # resetooo
        should_ignore_override_set = set()
        self.occurences  = {}
        self.assisted_occurences = {}
        self.ignored_occurences = {}
        self.processed_text = {}
        self.rejected_text = {}

        for label_to_track in labels_to_track:

            if label_to_track in label_and_boxes:
                continue
            if label_to_track not in self.config[TRACKING_CONFIGURATIONS_KEY]:
                print('unsupported label', label_to_track)
                continue

            text_track_key = '%s_%s_%s_text_trackable_label' % (self.user_id, self.session_id, label_to_track)

            text_track_configuration = self.config[TRACKING_CONFIGURATIONS_KEY][label_to_track]
            text_track_rect = text_track_configuration[OCR_RECT_KEY]
            ocr_config = None
            if OCR_CONFIG_KEY in text_track_configuration:
                ocr_config = text_track_configuration[OCR_CONFIG_KEY]


            text_frame = self.get_subframe_from_frame(text_track_rect, frame)

            # check for ignore triggers
            if IGNORE_IF_TRIGGERS_KEY in text_track_configuration:
                override_data = text_track_configuration[IGNORE_IF_TRIGGERS_KEY]
                base_override_threshold = 0.05
                if THRESHOLD_KEY in override_data:
                    base_override_threshold = override_data[THRESHOLD_KEY]

                # check for overrides
                should_ignore_override, _ = TextTracker.text_override_in_frame(frame, override_data[RECTS_KEY], base_override_threshold)

                if should_ignore_override:
                    if frame_key not in self.ignored_occurences:
                        self.ignored_occurences[frame_key] = []

                    if label_to_track not in self.ignored_occurences[frame_key]:
                        self.ignored_occurences[frame_key].append(label_to_track)

                    if frame_key not in self.occurences:
                        self.occurences[frame_key] = []

                    if label_to_track not in self.text_counts:
                        self.text_counts[label_to_track] = 0

                    if label_to_track not in self.occurences[frame_key]:
                        self.occurences[frame_key].append(label_to_track)
                    self.text_counts[label_to_track] += 1

                    should_ignore_override_set.add(label_to_track)


            if OVERRIDE_RECTS_KEY not in text_track_configuration:
                continue

            base_threshold = 0.95
            if THRESHOLD_KEY in text_track_configuration:
                base_threshold = text_track_configuration[THRESHOLD_KEY]

            # check for overrides
            override_for_text, _ = TextTracker.text_override_in_frame(frame, text_track_configuration[OVERRIDE_RECTS_KEY], base_threshold)

            #an assist did happen
            did_assist_in_detection = did_assist_in_detection or override_for_text

            if did_assist_in_detection:
                assist_labels.append(label_to_track)

                # add rect to labels and boxes.
                rect_for_assist = text_track_configuration[RECT_KEY]
                if ASSISTED_LABEL_RECT_KEY in text_track_configuration:
                    rect_for_assist = text_track_configuration[ASSISTED_LABEL_RECT_KEY]

                label_and_boxes[label_to_track] = [rect_for_assist]
                if frame_key not in self.assisted_occurences:
                    self.assisted_occurences[frame_key] = []

                if label_to_track not in self.assisted_occurences[frame_key]:
                    self.assisted_occurences[frame_key].append(label_to_track)

        # second pass
        for label_to_track in labels_to_track:
            if label_to_track not in label_and_boxes:
                continue
            if label_to_track in should_ignore_override_set:
                continue

            if label_to_track not in self.config[TRACKING_CONFIGURATIONS_KEY]:
                print('unsupported label', label_to_track)
                continue

            text_track_configuration = self.config[TRACKING_CONFIGURATIONS_KEY][label_to_track]

            ignore_based_on_label = False
            if IGNORE_IF_LABELS_EXIST_KEY in text_track_configuration:
                for ignore_label in text_track_configuration[IGNORE_IF_LABELS_EXIST_KEY]:
                    if ignore_label in label_and_boxes:
                        ignore_based_on_label = True
            if ignore_based_on_label:
                if frame_key not in self.ignored_occurences:
                    self.ignored_occurences[frame_key] = []

                if label_to_track not in self.ignored_occurences[frame_key]:
                    self.ignored_occurences[frame_key].append(label_to_track)
                continue

            if frame_key not in self.occurences:
                self.occurences[frame_key] = []

            if label_to_track not in self.text_counts:
                self.text_counts[label_to_track] = 0

            if label_to_track not in self.occurences[frame_key]:
                self.occurences[frame_key].append(label_to_track)
            self.text_counts[label_to_track] += 1

            text_track_rect = text_track_configuration[RECT_KEY]
            message_frame = self.get_subframe_from_frame(text_track_rect, frame)
            retval, buffer = cv2.imencode('.png', message_frame)

            text_img_bytes = np.array(buffer).tostring()

            last_message_bytes = self.update_and_get_last_message_frame(text_img_bytes, label_to_track)
            message_similarities = last_message_bytes is not None

            ocr_config = {}
            if OCR_CONFIG_KEY in text_track_configuration:
                ocr_config = text_track_configuration[OCR_CONFIG_KEY]

            restricted_regex = None
            if IGNORE_IF_REGEX_TRIGGERED_KEY in text_track_configuration:
                restricted_regex = text_track_configuration[IGNORE_IF_REGEX_TRIGGERED_KEY]

            if last_message_bytes is not None:
                last_message_frame = np.array(Image.open(io.BytesIO(last_message_bytes)))

                message_similarities = self.calculate_similar_frame_ratio(last_message_frame, message_frame)

                if REJECT_DUPLICATE_MESSAGES and( last_message_bytes is not None and message_similarities >= 0.95):
                    print('Rejecting frame for duplicate message')
                    self.save_message_img(message_frame, accepted=False)
                else:
                    self.save_message_img(message_frame, accepted=True)
                    future = self.pool.apply_async(self.extract_english_japanese_text, [frame_key, message_frame, ocr_config, label_to_track, restricted_regex], callback=self.construct_pokemon_info_page_1)
                    self.futures.append(future)

            else:
                self.save_message_img(message_frame, accepted=True)
                future = self.pool.apply_async(self.extract_english_japanese_text, [frame_key, message_frame, ocr_config, label_to_track, restricted_regex], callback=self.construct_pokemon_info_page_1)

        self.save_state(frame_key)
        return label_and_boxes, assist_labels


    def update_and_get_last_message_frame(self, current_frame, label):
        last_text_track_key = '%s_%s_%s_last_text_trackable_label' % (self.user_id, self.session_id, label)

        if self.use_redis:
            last_frame = self.messages_r.get(last_text_track_key)

            self.messages_r.set(last_text_track_key, current_frame)

            return last_frame
        else:
            if last_text_track_key in self.last_frame_mapping:
                return self.last_frame_mapping[last_text_track_key]

        return None

    def clear_last_message_frame(self, label):
        last_text_track_key = '%s_%s_%s_last_text_trackable_label' % (self.user_id, self.session_id, label)

        if self.use_redis:
            self.r.delete(last_text_track_key)
        else:
            self.last_frame_mapping[last_text_track_key] = None

    @staticmethod
    def get_subframe_from_frame(rect, source_frame):
        h, w, c = source_frame.shape
        x1, y1, x2, y2 = rect
        x1 = min(max(x1, 0), w)
        x2 = min(max(x2, 0), w)
        y1 = min(max(y1, 0), h)
        y2 = min(max(y2, 0), h)
        crop_img = source_frame[y1:y2, x1:x2]
        print('x1, y1, x2, y2', x1, y1, x2, y2)
        return crop_img

    def add_messages_to_session(self, messages, label):
        if self.use_redis:
            # store for csv
            messages_key = "%s:%s:%s_messages_text_tracker" % (self.user_id, self.session_id, label)
            self.r.rpush(messages_key, json.dumps(messages))
        else:
            self.stored_messages_for_local.append(messages)

    def get_messages_for_label(self, label):
        if self.use_redis:
            # store for csv
            messages_key = "%s:%s:%s_messages_text_tracker" % (self.user_id, self.session_id, label)
            messages_strs =  self.r.lrange(messages_key, 0, -1)


            messages = []
            for item in messages_strs:
                messages.append(json.loads(item))

            messages_count = len(messages)
            if messages_count > 0:
                # wipe queue
                self.r.ltrim(messages_key, messages_count, -1)


            return messages
        else:
            messages = self.stored_messages_for_local.copy()
            self.stored_messages_for_local = []
            return messages

    def any_messages_pending_for_label(self, label):
        if self.use_redis:
            # store for csv
            messages_key = "%s:%s:%s_messages_text_tracker" % (self.user_id, self.session_id, label)
            messages_strs =  self.r.lrange(messages_key, 0, -1)

            messages = []
            for item in messages_strs:
                messages.append(json.loads(item))

            messages_count = len(messages)

            return messages_count > 0
        else:
            return len(self.stored_messages_for_local)

    @staticmethod
    def extract_english_japanese_text(frame_key, frame, ocr_config, label, regex=None):
#    def extract_english_japanese_text(self, frame):
        try:
            print('inside of extracto magneto')
            messages = PytesseractManager.process_image_for_text(frame, ocr_config)
        except Exception as e:
            print('Error occurred: %s ' % str(e))
            print(e)
            raise e
        return frame_key, messages, regex, label

    def construct_pokemon_info_page_1(self, future):
        frame_key, messages, regexes, label = future
        if frame_key not in self.processed_text:
            self.processed_text[frame_key] = {}

        if label not in self.processed_text[frame_key]:
            self.processed_text[frame_key][label] = []

        self.processed_text[frame_key][label].append(messages)

        self.messages_in_order.append((frame_key, label, messages))

        if regexes is None:
            self.add_messages_to_session(messages, label)
        else:
            for message in messages:
                for regex in regexes:
                    if re.search(regex, message):
                        if frame_key not in self.rejected_text:
                            self.rejected_text[frame_key] = {}

                        if label not in self.rejected_text[frame_key]:
                            self.rejected_text[frame_key][label] = []

                        self.rejected_text[frame_key][label].append(messages)
                        self.all_rejected_messages.append((frame_key, label, messages))
                        self.add_accept_reject_messages_to_session((frame_key, label, messages), False)
                        return
            self.add_messages_to_session(messages, label)
        self.all_accepted_messages.append((frame_key, label, messages))

        self.add_accept_reject_messages_to_session((frame_key, label, messages), True)
        self.save_state(frame_key)


    def add_accept_reject_messages_to_session(self, messages_data, accepted):
        # store for csv
        messages_in_order_key = "%s:%s_messages_in_order" % (self.user_id, self.session_id)
        all_accepted_messages_in_order_key = "%s:%s_all_accepted_messages" % (self.user_id, self.session_id)
        all_rejected_messages_in_order_key = "%s:%s_all_rejected_messages" % (self.user_id, self.session_id)

        if self.use_redis:
            if accepted:
                self.r.rpush(all_accepted_messages_in_order_key, json.dumps(messages_data))
            else:
                self.r.rpush(all_rejected_messages_in_order_key, json.dumps(messages_data))
            self.r.rpush(messages_in_order_key, json.dumps(messages_data))
        else:
            pass

        return True


    def get_accept_reject_messages_for_session(self):
        # store for csv
        # store for csv
        messages_in_order_key = "%s:%s_messages_in_order" % (self.user_id, self.session_id)
        all_accepted_messages_in_order_key = "%s:%s_all_accepted_messages" % (self.user_id, self.session_id)
        all_rejected_messages_in_order_key = "%s:%s_all_rejected_messages" % (self.user_id, self.session_id)

        if self.use_redis:
            messages_in_order_strs =  self.r.lrange(messages_in_order_key, 0, -1)
            all_accepted_messages_in_order_strs =  self.r.lrange(all_accepted_messages_in_order_key, 0, -1)
            all_rejected_messages_in_order_strs =  self.r.lrange(all_rejected_messages_in_order_key, 0, -1)

            messages_in_order = []
            for item in messages_in_order_strs:
                messages_in_order.append(json.loads(item))

            all_rejected_messages = []
            for item in all_rejected_messages_in_order_strs:
                all_rejected_messages.append(json.loads(item))

            all_accepted_messages = []
            for item in all_accepted_messages_in_order_strs:
                all_accepted_messages.append(json.loads(item))

            self.all_accepted_messages = all_accepted_messages
            self.all_rejected_messages = all_rejected_messages
            self.messages_in_order = messages_in_order
        else:
            pass


    @staticmethod
    def text_override_in_frame(img, rect_requirements, base_threshold):

        all_checks_pass = True
        print('checking text override')
        failure_data = {}

        for requirement in rect_requirements:
            threshold = base_threshold
            if IGNORE_IF_TRIGGERS_KEY in requirement:
                threshold = requirement[THRESHOLD_KEY]

            crop_dimens = requirement[RECT_KEY]
            lower =(requirement["min_max_red"][0], requirement["min_max_green"][0], requirement["min_max_blue"][0]) # lower bound for each channel
            upper =(requirement["min_max_red"][1], requirement["min_max_green"][1], requirement["min_max_blue"][1]) # lower bound for each channel


            left = crop_dimens[0]
            top = crop_dimens[1]
            width = crop_dimens[2]
            height = crop_dimens[3]
            crop = img[top:height, left:width]

            all_checks_pass = all_checks_pass and (TextTracker.calculate_rect_ratio(crop, lower, upper) >= threshold)

            if not all_checks_pass:
                failure_data['crop_dimens'] = crop_dimens
                failure_data['requirement'] = requirement
                failure_data['percent'] = TextTracker.calculate_rect_ratio(crop, lower, upper)
                print('crop_dimens', crop_dimens)
                print('requirement', requirement)
                print('percent', TextTracker.calculate_rect_ratio(crop, lower, upper))
                print()
                break

        return all_checks_pass, failure_data


    @staticmethod
    def calculate_rect_ratio(image, lower, upper):
        # make non grey pixels yellow
        img_adj = image.copy()

        # create the mask and use it to change the colors
        mask = cv2.inRange(img_adj, lower, upper)
        masked_color = [0,255,255]
        mask = 255 - mask
        img_adj[mask == 0] = masked_color
        return TextTracker.count_non_yellow_pixels(img_adj, masked_color)


    @staticmethod
    def count_non_yellow_pixels(image, mask):
        # grab the image dimensions
        h = image.shape[0]
        w = image.shape[1]
        target_pixels = 0


        # loop over the image, pixel by pixel
        for y in range(0, h):
            for x in range(0, w):
              pixel = image[y, x]
              if pixel[0] == mask[0] and pixel[1] == mask[1] and pixel[2] == mask[2]:
                target_pixels += 1
        return target_pixels / float(h*w)

    @staticmethod
    def calculate_similar_frame_ratio(imageData_1, imageData_2):

        valid_pixels_count = 0
        pixel_count = 0

        print('imageData_1 shape', imageData_1.shape)
        for i in range(0,imageData_1.shape[0]):
            for j in range(0,imageData_1.shape[1]):
                pixel_count += 1

                pixel_1 = [imageData_1.item(i, j, 0), imageData_1.item(i, j, 1), imageData_1.item(i, j, 2)]
                pixel_2 = [imageData_2.item(i, j, 0), imageData_2.item(i, j, 1), imageData_2.item(i, j, 2)]

                if pixel_1 == pixel_2:
                    valid_pixels_count += 1
        print('valid_pixels_count', valid_pixels_count)
        print('pixel_count', pixel_count)
        return valid_pixels_count / float(pixel_count)


    def save_message_img(self, message_frame, accepted):
        if not SAVE_MESSAGE_FRAMES:
            return

#        dir_to_use = '%s/%s' % (ACCEPTED_MESSAGE_DIR, self.state_manager.session_id)
        dir_to_use = ACCEPTED_MESSAGE_DIR
        if not accepted:
#            dir_to_use = '%s/%s' % (REJECTED_MESSAGE_DIR, self.state_manager.session_id)
            dir_to_use = REJECTED_MESSAGE_DIR

        if not os.path.exists(os.path.dirname(dir_to_use)):
            os.makedirs(os.path.dirname(dir_to_use))

        filename = '%s/%s.png' % (dir_to_use,  (str(uuid.uuid4())))
#        filename = '%s.png' % ((str(uuid.uuid4())))

        status = cv2.imwrite(filename, message_frame)


    @staticmethod
    def get_min_max_colors_for_regions_in_images(images, inspection_regions):

        black_min_red = 255
        black_max_red = 0
        black_min_green = 255
        black_max_green = 0
        black_min_blue = 255
        black_max_blue = 0

        result = []

        for crop_dimens in inspection_regions:
            left = crop_dimens[0]
            top = crop_dimens[1]
            width = crop_dimens[2]
            height = crop_dimens[3]

            for img in images:
                crop = img[top:height, left:width]

                # grab the image dimensions
                h = crop.shape[0]
                w = crop.shape[1]
                target_pixels = 0


                # loop over the image, pixel by pixel
                for y in range(0, h):
                    for x in range(0, w):

                        pixel = crop[y, x]
                        blue = pixel[0]
                        green = pixel[1]
                        red = pixel[2]

                        black_min_blue = int(min(black_min_blue, blue))
                        black_max_blue = int(max(black_max_blue, blue))
                        black_min_red = int(min(black_min_red, red))
                        black_max_red = int(max(black_max_red, red))
                        black_min_green = int(min(black_min_green, green))
                        black_max_green = int(max(black_max_green, green))

            for crop_dimens in inspection_regions:
                result.append({
                    "rect": crop_dimens,
                    "min_max_red": [black_min_red, black_max_red],
                    "min_max_green": [black_min_green, black_max_green],
                    "min_max_blue": [black_min_blue, black_max_blue],
                })

        return result



import json
import requests
import cv2
import numpy as np
import os


TESSERACT_BASE_URL = os.environ.get('TESSERACT_BASE_URL', 'http://localhost:5333/api/')
#TESSERACT_BASE_URL = os.environ.get('TESSERACT_BASE_URL', 'http://192.168.0.141:5333/api/')

class PytesseractManager():

    @staticmethod
    def fire_request( url, image, params):
        baseurl = TESSERACT_BASE_URL
        is_base64=False

        url = baseurl + url
        print('tesseract url:', url)

        if not is_base64:
#            headers = {'content-type': 'multipart/form-data'}

            _, image = cv2.imencode('.jpg', image)
            files = {
                'image': ('image', image, 'image/jpg'),
            }

            response = requests.post(url, data=params, files=files)

            return json.loads(response.text)['result']

        else:
            headers = {'content-type': 'application/json'}
            params['image'] =  image,

            response = requests.post(url, data=params, headers=headers)
            print('fire response', response)
            return json.loads(response.text)['result']

    @staticmethod
    def process_image_for_text( image, ocr_config=None):
        url = 'process_image_for_text'
        url = 'parse_rect_with_pytesseract_config'
        params = {}
        params['ocr_config'] = json.dumps(ocr_config)

        return PytesseractManager.fire_request(url, image, params)
