import Quartz  # noqa
import time


def bit(var, pos, val):
    return var | (1 << pos) if val else var & ~(1 << pos)


def action(code, mod, mask):
    code = code[2]

    if code == 59 or code == 62:
        mask = bit(mask, 0, mod)
    if code == 56 or code == 60:
        mask = bit(mask, 1, mod)
    if code == 58 or code == 61:
        mask = bit(mask, 2, mod)
    if code == 54 or code == 55:
        mask = bit(mask, 3, mod)
    if code == 57:
        mask = bit(mask, 4, mod)

    flags = 0
    if mask >> 0 & 1:
        flags += Quartz.kCGEventFlagMaskControl
    if mask >> 1 & 1:
        flags += Quartz.kCGEventFlagMaskShift
    if mask >> 2 & 1:
        flags += Quartz.kCGEventFlagMaskAlternate
    if mask >> 3 & 1:
        flags += Quartz.kCGEventFlagMaskCommand
    if mask >> 4 & 1:
        flags += Quartz.kCGEventFlagMaskAlphaShift

    event = Quartz.CGEventCreateKeyboardEvent(None, code, mod)
    Quartz.CGEventSetFlags(event, flags)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
    return mask


def press(code, mask):
    mask = action(code, True, mask)
    return mask


def release(code, mask):
    mask = action(code, False, mask)
    return mask


def sequence(codes, delay):
    mask = 0b00000  # ctrl, shift, alt, cmd, caps
    for code in codes:
        mask = press(code, mask)
        time.sleep(delay)
    codes.reverse()
    for code in codes:
        mask = release(code, mask)
        time.sleep(delay)
    return
