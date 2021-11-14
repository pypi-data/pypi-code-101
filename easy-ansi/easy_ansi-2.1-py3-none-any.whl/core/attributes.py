from easyansi.core import core as _core

# Font "Brightness"
# Bright and Dim send a normal ANSI code first because some terminals require this.
NORMAL = f"{_core.CSI}22m"

BRIGHT = f"{NORMAL}{_core.CSI}1m"
BRIGHT_ON = BRIGHT
BRIGHT_OFF = NORMAL

DIM = f"{NORMAL}{_core.CSI}2m"
DIM_ON = DIM
DIM_OFF = NORMAL

ITALIC = f"{_core.CSI}3m"
ITALIC_ON = ITALIC
ITALIC_OFF = f"{_core.CSI}23m"

UNDERLINE = f"{_core.CSI}4m"
UNDERLINE_ON = UNDERLINE
UNDERLINE_OFF = f"{_core.CSI}24m"

BLINK = f"{_core.CSI}5m"
BLINK_ON = BLINK
BLINK_OFF = f"{_core.CSI}25m"

REVERSE = f"{_core.CSI}7m"
REVERSE_ON = REVERSE
REVERSE_OFF = f"{_core.CSI}27m"

CONCEAL = f"{_core.CSI}8m"
CONCEAL_ON = CONCEAL
CONCEAL_OFF = f"{_core.CSI}28m"

STRIKETHROUGH = f"{_core.CSI}9m"
STRIKETHROUGH_ON = STRIKETHROUGH
STRIKETHROUGH_OFF = f"{_core.CSI}29m"

# This turns all above defined attributes off
ATTRIBUTES_OFF = f"{NORMAL}{ITALIC_OFF}{UNDERLINE_OFF}{BLINK_OFF}{REVERSE_OFF}{CONCEAL_OFF}{STRIKETHROUGH_OFF}"
