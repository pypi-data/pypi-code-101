from typing import Union

import filetype
import logging
import os
import re
import toml
import optilibre.enums as enums
import optilibre.helpers as helpers
from multiprocessing import Pool
from pathlib import Path


def build_cmdline_video(local_config: dict) -> str:
    """
    Build cmdline options
    :param local_config:
    :return: cmdline (without in and out files)
    """

    codec_video = get_codec(codec_str=str(local_config['video']['codec']), codec_type="video")

    # Set default options if not already set
    if "map_metadata" not in local_config['meta']:
        local_config['meta']['map_metadata'] = 0
    if "n" not in local_config['meta'] or "y" not in local_config['meta']:
        local_config['meta']['n'] = ''
    if codec_video == enums.VideoCodec.libx265 and "dst_range" not in local_config[codec_video.name]:
        # enable full color range for x265 per default
        local_config[codec_video.name]['dst_range'] = 1

    # Build cmdline
    cmdline_meta = ""
    if 'meta' in local_config:
        for opt in local_config['meta'].items():
            cmdline_meta += " -" + str(opt[0]) + " " + str(opt[1])

    cmdline_audio = ""
    if local_config['audio']['enabled']:
        cmdline_audio = "-c:a " + str(local_config['audio']['codec'])

    cmdline_video = ""
    if local_config['video']['enabled']:
        cmdline_video = "-c:v " + codec_video.name
        for opt in local_config[local_config['video']['codec']].items():
            cmdline_video += " -" + str(opt[0]) + " " + str(opt[1])

    return "ffmpeg -i " + "%s" + cmdline_meta + " " + cmdline_audio + " " + cmdline_video + " " + "%s"


def get_local_config(conf, file_name="optilibre.toml") -> dict:
    """
    Open and read local (folder specific) config file
    :param conf: main config file
    :param file_name: name where codec config resides.
    :return: local config file
    """
    try:
        with open(os.path.join(conf['path'], file_name), 'r') as f:
            local_config = toml.load(f)
    except OSError or FileNotFoundError:
        logging.exception("Could not find %s conf file for %s." % (file_name, str(conf['path'])))
        local_config = None

        # EXIT
        exit(1)

    return local_config


def get_codec(codec_str: "", codec_type: str) -> Union[enums.ImageCodec, enums.VideoCodec]:
    """
    Convert str to codec as enum
    :param codec_str: codec name
    :param codec_type: is video or image
    :return: codec (enum)
    """
    codec = None
    if codec_type == "video":
        try:
            codec = enums.VideoCodec[codec_str.lower()]
        except KeyError:
            logging.error("%s is not a supported image codec." % codec)
            raise KeyError
    else:
        try:
            codec = enums.ImageCodec[codec_str.lower()]
        except KeyError:
            logging.error("%s is not a supported video codec." % codec)
            raise KeyError

    return codec


def convert_img(file: Path, shell_cmdline: str, local_config: dict):
    logging.debug("Converting " + str(file))

    # TODO move file extension / output
    logging.info(shell_cmdline)
    exit_code = os.WEXITSTATUS(os.system(shell_cmdline))
    logging.debug("Exit code: %s" % exit_code)
    helpers.do_src_on_done(exit_code=exit_code, file=file, local_config=local_config)


def process_image_folder(name: str, conf: dict):
    logging.info("Treating folder: " + name)

    local_config = get_local_config(conf)['optiimage']
    if local_config is None:
        logging.error("No local configuration given. Aborting.")
        # RETURN
        return

    out_path = local_config['out_path']
    if not os.path.exists(out_path) or not os.path.isdir(out_path):
        logging.error("Out path (%s) doesn't exist or is not a directory." % out_path)
        # RETURN
        return

    codec = local_config['codec']
    codec = get_codec(codec_str=codec, codec_type="image")

    # Set default options
    if codec == enums.ImageCodec.jpeg:
        if "d" not in local_config[codec.name.lower()] and "dest" not in local_config[codec.name.lower()]:
            local_config[codec.name.lower()]['d'] = out_path

    # Build cmdline options
    cmdline_codec_opts = ""
    if codec.name.lower() in local_config:
        for opt in local_config[codec.name.lower()].items():
            cmdline_codec_opts += " -" + str(opt[0]) + " " + str(opt[1])
    else:
        logging.debug("No config for %s found. Using default codec values." % codec.name)

    arg_list = []  # [(file1, shell1, local_config), (...)]
    for file in Path(conf['path']).glob('*'):
        logging.debug("Building cmd line for: %s" % str(file))
        file_mime = filetype.guess_mime(str(file))

        if file.suffix not in optilibre.supported_img_ext or not bool(re.match('image/+', str(file_mime))):
            # TODO Jpeg-XL can convert non jpeg format.
            logging.warning("Filetype: %s not supported: for file: %s. Won't convert it." % (str(file_mime), str(file)))
            # CONTINUE
            continue

        if codec == enums.ImageCodec.jpeg:
            encoder_cmdline = "jpegoptim"
            out_file = ""
        elif codec == enums.ImageCodec.jpegxl:
            encoder_cmdline = "cjxl"
            out_file = os.path.join(out_path, os.path.splitext(os.path.basename(file))[0] + ".jxl")
        else:
            logging.error("Codec type not supported %s" % str(codec))
            # CONTINUE
            continue

        shell_cmdline = "{encoder} {in_file} {options} {outfile}".format(encoder=encoder_cmdline, in_file=str(file),
                                                                         options=cmdline_codec_opts, outfile=out_file)

        arg_list += (file, shell_cmdline, local_config)

    if arg_list:
        with Pool() as p:
            # multiprocess call
            p.starmap(convert_img, [arg_list])


def process_video_folder(name: str, conf: dict):
    logging.info("Treating folder: " + name)

    local_config = get_local_config(conf)['optivideo']
    if local_config is None:
        # Return
        raise KeyError

    out_path = local_config['out_path']
    if not os.path.exists(out_path) or not os.path.isdir(out_path):
        logging.error("Out path (%s) doesn't exist or is not a directory." % out_path)
        # RETURN
        return

    cmdline = build_cmdline_video(local_config=local_config)

    for file in Path(conf['path']).glob('*'):
        logging.debug("Processing " + str(file))
        kind = filetype.guess_mime(str(file))

        if bool(re.match("video/+", str(kind))):
            if file.suffix in optilibre.supported_video_ext:
                out_file = os.path.join(out_path, os.path.basename(file))
                ffmpeg_cmdline = cmdline.format(file, out_file)

                logging.info(ffmpeg_cmdline)
                exit_code = os.WEXITSTATUS(os.system(ffmpeg_cmdline))
                helpers.do_src_on_done(exit_code=exit_code, file=file, local_config=local_config)

            else:
                logging.info("Filetype %s is not (yet) supported." % str(file.suffix))
        else:
            logging.debug("Filetype: %s for file: %s isn't a video file." % (str(kind), str(file)))


def main(config_file):
    logging.info("Reading " + config_file)
    with open(config_file, 'r') as f:
        config = toml.load(f)

    for c in config['convert']['video']:
        try:
            process_video_folder(c, config['convert']['video'][c])
        except FileNotFoundError or KeyError:
            logging.exception("Failed to process %s." % c)

    for c in config['convert']['image']:
        try:
            process_image_folder(c, config['convert']['image'][c])
        except FileNotFoundError or KeyError:
            logging.exception("Failed to process %s." % c)
