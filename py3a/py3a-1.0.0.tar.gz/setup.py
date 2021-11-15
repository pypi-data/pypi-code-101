# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py3a', 'py3a.py3a', 'py3a.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py3a',
    'version': '1.0.0',
    'description': 'Lib for reading and writing 3a format',
    'long_description': '# py3a\nThis library provides a structural representation of [3a ascii animations format](https://github.com/DomesticMoth/3a) and methods for reading and writing it.  \nThis lib on [pypi](https://pypi.org/project/py3a) \n- [Usage](#usage)\n- [Short API description](#short-api-description)\n  - [Structs](#structs)\n  - [Functions](#functions)\n## Usage\nInstall  \n```\n$ pip install py3a\n```\nHere\'s a simple example that parsing a string in 3a format and displaying a header:  \n```python\nimport py3a\n\nCOLORTABLE_EXAMPLE = """\t\nwidth 32\nheight 19\nloop false\ncolors full\ntitle colortable demo\nauthor Moth\n\nin \' ab \'                       ffffffffffffffffffffffffffffffff00000000000000000000000000000000\na-foreground, b-background      ffffffffffffffffffffffffffffffff00000000000000000000000000000000\n                                ffffffffffffffffffffffffffffffff00000000000000000000000000000000\n 00  01  02  03  04  05  06  07 0000000000000000000000000000000000001111222233334444555566667777\n 10  11  12  13  14  15  16  17 1111111111111111111111111111111100001111222233334444555566667777\n 20  21  22  23  24  25  26  27 2222222222222222222222222222222200001111222233334444555566667777\n 30  31  32  33  34  35  36  37 3333333333333333333333333333333300001111222233334444555566667777\n 40  41  42  43  44  45  46  47 4444444444444444444444444444444400001111222233334444555566667777\n 50  51  52  53  54  55  56  57 5555555555555555555555555555555500001111222233334444555566667777\n 60  61  62  63  64  65  66  67 6666666666666666666666666666666600001111222233334444555566667777\n 70  71  72  73  74  75  76  77 7777777777777777777777777777777700001111222233334444555566667777\n 80  81  82  83  84  85  86  87 8888888888888888888888888888888800001111222233334444555566667777\n 90  91  92  93  94  95  96  97 9999999999999999999999999999999900001111222233334444555566667777\n a0  a1  a2  a3  a4  a5  a6  a7 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa00001111222233334444555566667777\n b0  b1  b2  b3  b4  b5  b6  b7 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb00001111222233334444555566667777\n c0  c1  c2  c3  c4  c5  c6  c7 cccccccccccccccccccccccccccccccc00001111222233334444555566667777\n d0  d1  d2  d3  d4  d5  d6  d7 dddddddddddddddddddddddddddddddd00001111222233334444555566667777\n e0  e1  e2  e3  e4  e5  e6  e7 eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00001111222233334444555566667777\n f0  f1  f2  f3  f4  f5  f6  f7 ffffffffffffffffffffffffffffffff00001111222233334444555566667777"""\n\n\nif __name__ == "__main__":\n    art = py3a.Art.load(COLORTABLE_EXAMPLE)\n    print(art.header)\n```\n## Short API description\n### Structs\nThe core of the library is the Art class, which implements the 3a structure:  \n```python\nclass Art:\n    def __init__ (self, header: Header, body: Body):\n        self.header = header\n        self.body = body\n```\nHeader type contains information about the header of 3a file:  \n```python\nclass Header:\n    def __init__ (self, width: int, height: int, delay: int, loop_enable: bool, color_mod: ColorMod,\n                    utf8: bool, datacols: int, preview: int, audio: str, title: str, author: str):\n        self.width = width\n        self.height = height\n        self.delay = delay\n        self.loop_enable = loop_enable\n        self.color_mod = color_mod\n        self.utf8 = utf8\n        self.datacols = datacols\n        self.preview = preview\n        self.audio = audio\n        self.title = title\n        self.author = author\n```\nBody class contains a list of frames, where each frame is a list of rows, and each row is a list of row fragments:  \n```python\nRow = typing.List[RowFragment]\n\nFrame = typing.List[Row]\n\nclass Body:\n    def __init__ (self, frames: typing.List[Frame] ):\n        self.frames = frames\n```\nEach RowFragment is a set of consecutive symbols with the same values of foreground and background colors:  \n```python\nclass RowFragment:\n    def __init__ (self, text: str, fg_color: Color, bg_color: Color):\n        self.text = text\n        self.fg_color = fg_color\n        self.bg_color = bg_color\n```\n### Methods\n`Art.load` and `art.save` methods allow you to convert strings to `Art` and back.  \n`Art.load_file` and `art.save_file` methods allow you to read 3a files to `Art` and write `Art` to 3a files.  \n',
    'author': 'DomesticMoth',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DomesticMoth/py3a',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
