from IPython.core.magic import Magics, magics_class, line_cell_magic
from IPython.display import IFrame, display
import urllib
import re


@magics_class
class TutorMagics(Magics):
    @line_cell_magic
    def tutor(self, line, cell=None):
        """
        Python Tutor IPython magic extension

        Magic methods:
            %%tutor
            < python code ... >

            %tutor filename

            %%tutor 640x400
            < python code ... >

            %tutor 640x400 filename
        """
        (width, height, filename) = (None, None, None)
        source = cell
        m = re.match(r" *(?:(\d+).(\d+))? *(.*)", line)
        if m:
            (width, height, filename) = m.groups()
            if filename:
                source = open(filename).read()
            else:
                source = cell
        if not width or not height:
            (width, height) = ("100%", 500)
        payload = urllib.parse.urlencode({"code": source, "py": "3"})
        url = f"https://pythontutor.com/iframe-embed.html#{payload}&rawInputLstJSON=%5B%5D"
        display(
            IFrame(
                url,
                width,
                height,
                extras=['frameborder="0"'],
            )
        )