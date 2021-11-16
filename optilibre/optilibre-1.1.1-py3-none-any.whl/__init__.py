import coloredlogs
import logging
import importlib.metadata

__version__ = importlib.metadata.version('optilibre')
coloredlogs.install(level=logging.DEBUG)

supported_img_ext = [".jpeg", ".jpg", ".jpegxl", ".jxl"]
supported_video_ext = [".mp4", ".mkv"]
