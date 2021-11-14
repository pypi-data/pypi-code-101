def byte_to_bit_list(byte: int):
    if not (0 <= byte <= 255):
        raise ValueError('Byte must be between 0 and 255!')

    bits = [(byte & (0x01 << i)) != 0 for i in range(8)]
    bits.reverse()
    return bits


def bit_list_to_byte(bits: list[bool]):
    if len(bits) != 8 or not all([isinstance(i, bool) for i in bits]):
        raise ValueError('Must provide exactly 8 bits (1 byte)!')

    byte = 0
    for bit in bits:
        byte = byte << 1 | (1 if bit else 0)
    return byte


def set_bit(byte: int, pos: int, val: bool):
    if not (0 <= byte <= 255):
        raise ValueError('Byte must be between 0 and 255!')
    if not (0 <= pos <= 7):
        raise ValueError('Position must be between 0 and 7!')
    if not isinstance(val, bool):
        raise ValueError('Bit must be a boolean!')

    mask = ~(1 << pos)
    return (byte & mask) | (val << pos)


def get_bit(byte: int, pos: int):
    if not (0 <= byte <= 255):
        raise ValueError('Byte must be between 0 and 255!')
    if not (0 <= pos <= 7):
        raise ValueError('Position must be between 0 and 7!')

    return (byte & (1 << pos)) != 0
