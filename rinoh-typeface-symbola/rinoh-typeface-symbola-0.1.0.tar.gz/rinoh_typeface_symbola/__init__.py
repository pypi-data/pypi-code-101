from os import path

from rinoh.font import Typeface
from rinoh.font.opentype import OpenTypeFont


__all__ = ["typeface"]


# font files were downloaded from https://fontlibrary.org/en/font/symbola


def otf(ttf_name):
    filename = f"{ttf_name}.ttf"
    return path.join(path.dirname(__file__), filename)


typeface = Typeface(
    "Symbola",
    OpenTypeFont(otf("Symbola")),
)
