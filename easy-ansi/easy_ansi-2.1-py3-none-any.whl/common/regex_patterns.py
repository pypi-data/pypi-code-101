import re

# Source of CSI format: https://en.wikipedia.org/wiki/ANSI_escape_code
#   CSI Starting Sequence = Esc + [
#   CSI Parameter Bytes: 0–9 : ; < = > ?
#   CSI Intermediate Bytes: [space] ! " # $ % & ' ( ) * + , - . /
#   CSI Final Byte: A-Z a-z @ [ \ ] ^ _ ` { | } ~
ALL_CSI_REGEX = r'(\x1B\[)[0-?]*[ -\/]*[@-~]'
ALL_CSI_PATTERN = re.compile(ALL_CSI_REGEX)  # compile csi regex pattern

BELL_REGEX = r'\x07'
BELL_PATTERN = re.compile(BELL_REGEX)

OSC_TITLE_REGEX = r'(.*)(\x1B\][012];)(.*)(\x1B\\|\x07)(.*)'
OSC_TITLE_PATTERN = re.compile(OSC_TITLE_REGEX)
