"""Hide text in plain sight using invisible zero-width characters. It’s digital steganography made simple."""


from typing import Optional


__version__ = '1.0.0'


# todo: console entry points cause why not


HIDDEN_MAPPING = {
    # Unicode Character 'WORD JOINER' (U+2060)
    ' ': '\u2060',
    # Unicode Character 'ZERO WIDTH SPACE' (U+200B)
    '0': '\u200B',
    # Unicode Character 'ZERO WIDTH NON-JOINER' (U+200C)
    '1': '\u200C',
}


def wrap(string: str) -> str:
    """Wrap a string with a distinct boundary."""
    # Unicode Character 'ZERO WIDTH NON-BREAKING SPACE' (U+FEFF)
    return f'\uFEFF{string}\uFEFF'


def unwrap(string: str) -> Optional[str]:
    """Unwrap a string if the distinct boundary exists.

    Returns None if the distinct boundary does not exist.
    """
    temp = string.split('\uFEFF')

    if len(temp) == 1:
        return
    return temp[1]


def str2bin(text: str) -> str:
    """Convert a string into binary data."""
    return ' '.join(format(i, 'b') for i in bytearray(text, 'utf-8'))


def bin2str(binary: str) -> str:
    """Convert binary data into a string."""
    return ''.join(chr(int(i, 2)) for i in binary.split())


def bin2hidden(string: str) -> str:
    """Convert the ones, zeros, and spaces of the hidden binary data to their respective zero-width characters."""
    for char, zero_width in HIDDEN_MAPPING.items():
        string = string.replace(char, zero_width)
    return string


def hidden2bin(string: str) -> str:
    """Convert zero-width characters to hidden binary data."""
    for char, zero_width in HIDDEN_MAPPING.items():
        string = string.replace(zero_width, char)
    return string


def encode(public: str, private: str) -> str:
    """Hide a private message within a public message."""
    half = round(len(public) / 2)

    private_bin = str2bin(private)
    private_zero_width = bin2hidden(private_bin)
    private_wrapped = wrap(private_zero_width)

    public_steganographised = ''.join([public[:half], private_wrapped, public[half:]])
    return public_steganographised


def decode(public: str) -> Optional[str]:
    """Reveal the private message hidden within a public message.

    Returns None if no private message is found.
    """
    unwrapped = unwrap(public)

    if unwrapped is None:
        message = bin2str(hidden2bin(public))
    else:
        message = bin2str(hidden2bin(unwrapped))

    if len(message) < 2:
        # message = 'Notice: No private message was found.'
        return

    return message


if __name__ == '__main__':
    # informal tests
    wrapped = wrap('test')
    print(wrapped)
    print(wrapped.split('\uFEFF'))
    print(unwrap(wrapped))

    encoded = encode('hello world', 'never gonna give you up')
    print(encoded)
    print(decode(encoded))
