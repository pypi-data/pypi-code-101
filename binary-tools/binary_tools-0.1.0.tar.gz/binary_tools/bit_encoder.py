import math

from binary_tools import binary_util


class BitEncoder:
    def __init__(self):
        self.__buf = [False, False, False, False]
        self.__data = b''

    def __encode(self):
        full_bytes = math.floor(len(self.__buf) / 8)

        for i in range(full_bytes):
            self.__data += binary_util.bit_list_to_byte(self.__buf[i*8:i*8+8]).to_bytes(1, 'big')
            self.__buf = self.__buf[i+8:]

    def put_bit(self, bit: bool):
        if not isinstance(bit, bool):
            raise ValueError('Bit must be a bool value!')

        self.__buf.append(bit)
        self.__encode()

    def put_bits(self, bits: list[bool]):
        if not isinstance(bits, list) or not all([isinstance(i, bool) for i in bits]):
            raise ValueError('Must provide list of bits (bool values)!')

        for bit in bits:
            self.put_bit(bit)

    def put_byte(self, byte: int):
        if not (0 <= byte <= 255):
            raise ValueError('Byte must be between 0 and 255!')

        self.put_bits(binary_util.byte_to_bit_list(byte))

    def put_bytes(self, bs: bytes):
        if not isinstance(bs, bytes):
            raise ValueError('Must provide a byte string!')

        for b in bs:
            self.put_byte(b)

    def finalise(self):
        self.__encode()

        remaining_bits = len(self.__buf)

        if remaining_bits == 0:
            return self.__data

        last_byte = 0x00
        for i in range(remaining_bits):
            last_byte = binary_util.set_bit(last_byte, 7 - i, self.__buf[i])
        self.__data += last_byte.to_bytes(1, 'big')

        head = remaining_bits << 4 | self.__data[0]

        return head.to_bytes(1, 'big') + self.__data[1:]


class BitDecoder:
    def __init__(self, data: bytes):
        if not isinstance(data, bytes):
            raise ValueError('Must provide a byte string!')

        self.__buf = []

        head = data[0]
        remaining_bits = head >> 4
        actual_head_bits = binary_util.byte_to_bit_list(head & 0x0F)[4:]
        self.__buf.extend(actual_head_bits)

        data = data[1:]

        for b in data:
            self.__buf.extend(binary_util.byte_to_bit_list(b))

        if remaining_bits > 0:
            self.__buf = self.__buf[:-(8-remaining_bits)]

    def advance_bits(self, count: int):
        self.__buf = self.__buf[count:]

    def advance_bytes(self, count: int):
        self.advance_bits(count * 8)

    def has_more(self):
        return len(self.__buf) > 0

    def as_bit_list(self):
        return self.__buf

    def as_bytes(self):
        full_bytes = math.floor(len(self.__buf) / 8)

        byte_string = b''
        for i in range(full_bytes):
            byte_string += binary_util.bit_list_to_byte(self.__buf[i*8:i*8 + 8]).to_bytes(1, 'big')

        return byte_string
