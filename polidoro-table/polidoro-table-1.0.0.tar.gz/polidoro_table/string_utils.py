from enum import Enum


class Align(Enum):
    LEFT = '<'
    RIGHT = '>'
    CENTER = '^'


class Format(Enum):
    NORMAL = '\x1b[0m'
    BOLD = '\x1b[1m'
    DIM = '\x1b[2m'
    UNDERLINE = '\x1b[4m'
    BLINK = '\x1b[5m'
    REVERSE = '\x1b[7m'
    STRIKE = '\x1b[9m'

    def __str__(self):
        return self.value


class Color(Enum):
    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN = "\x1b[36m"
    WHITE = "\x1b[37m"

    LIGHT_BLACK = "\x1b[90m"
    LIGHT_RED = "\x1b[91m"
    LIGHT_GREEN = "\x1b[92m"
    LIGHT_YELLOW = "\x1b[93m"
    LIGHT_BLUE = "\x1b[94m"
    LIGHT_MAGENTA = "\x1b[95m"
    LIGHT_CYAN = "\x1b[96m"
    LIGHT_WHITE = "\x1b[97m"

    # class Fundo(Enum):
    #     """ Cores do Fundo do terminal """
    #
    #     BLACK = "\x1b[40m"
    #     RED = "\x1b[41m"
    #     GREEN = "\x1b[42m"
    #     YELLOW = "\x1b[43m"
    #     BLUE = "\x1b[44m"
    #     MAGENTA = "\x1b[45m"
    #     CYAN = "\x1b[46m"
    #     WHITE = "\x1b[47m"
    #
    #     LIGHT_BLACK = "\x1b[100m"
    #     LIGHT_RED = "\x1b[101m"
    #     LIGHT_GREEN = "\x1b[102m"
    #     LIGHT_YELLOW = "\x1b[103m"
    #     LIGHT_BLUE = "\x1b[104m"
    #     LIGHT_MAGENTA = "\x1b[105m"
    #     LIGHT_CYAN = "\x1b[106m"
    #     LIGHT_WHITE = "\x1b[107m"

    def __str__(self):
        return self.value


def fill(text, size, align=None, char=' '):
    align = align or Align.RIGHT
    return '{0:{char}{align}{size}}'.format(text, char=char, align=align.value, size=size)