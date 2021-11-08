import sys
from pgzero.runner import prepare_mod, run_mod
from pgzero.constants import keys

from pzwin.WinBase import WinBase


def draw():
    WinBase.g_pzwinDeskTop.draw()


def update():
    WinBase.dispatch()


def on_mouse_move(pos, rel, buttons):
    if len(buttons) == 0:
        WinBase.pumpMouseMoveEvent(pos)
    else:
        WinBase.pumpMouseDragStartEvent(rel, buttons)


def on_mouse_down(pos, button):
    WinBase.pumpMouseDownEvent(pos, button)


def on_mouse_up(pos, button):
    WinBase.pumpMouseUpEvent(pos, button)


def on_key_down(key: keys, mod, unicode):
    WinBase.keyDown(key, mod, unicode)


def on_key_up(key: keys, mod):
    WinBase.keyUp(key, mod)


def entryLoop():
    entryMod = sys.modules['pzwin.pgzeroEntry']
    setattr(entryMod, 'WIDTH', WinBase.g_desktopSize[0])
    setattr(entryMod, 'HEIGHT', WinBase.g_desktopSize[1])
    prepare_mod(entryMod)
    run_mod(entryMod)
