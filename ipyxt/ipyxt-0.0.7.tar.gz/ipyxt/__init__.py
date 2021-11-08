from IPython.core.magic import (register_line_magic,
                                register_cell_magic)

from IPython import get_ipython
from IPython.display import Audio
from IPython.core.display import display
import os


class MyAudio(Audio):
    def _repr_html_(self):
        src = """
                <audio hidden {element_id} controls="controls" {autoplay}>
                    <source src="{src}" type="{type}" />
                    Your browser does not support the audio element.
                </audio>
              """
        return src.format(src=self.src_attr(), type=self.mimetype, autoplay=self.autoplay_attr(),
                          element_id=self.element_id_attr())


def play(sound_file):
    #print(sound_file)
    audio = MyAudio(sound_file, autoplay=True)
    display(audio)

def _path():
    return os.path.dirname(os.path.realpath(__file__))

def ding():
    file_name = os.path.join(_path(), 'ding.mp3')
    play(file_name)


def crash():
    file_name = os.path.join(_path(), 'error.mp3')
    play(file_name)


@register_cell_magic
def run_loud(line, cell):
    result = get_ipython().run_cell(cell)
    if result.success:
        ding()
    else:
        crash()
        # result.raise_error()