import coloredlogs
import logging
import optilibre.cli as cli

coloredlogs.install(level=logging.DEBUG)

supported_img_ext = [".jpeg", ".jpg", ".jpegxl", ".jxl"]
supported_video_ext = [".mp4", ".mkv"]
