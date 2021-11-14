from binary_tools import bit_encoder


def _string_len(data: bytes):
    pos = 0
    while len(data) > pos and data[pos] != 0x00:
        pos += 1
    return pos


class ByteEncoder:
    def __init__(self):
        self.__bit_buf = bit_encoder.BitEncoder()

    def put_string(self, string: str):
        binarised_str = string.encode('ascii') + b'\x00'
        self.__bit_buf.put_bytes(binarised_str)

    def put_int(self, number: int, length: int):
        binarised_int = int.to_bytes(number, length, 'big')
        self.__bit_buf.put_bytes(binarised_int)

    def put_bool(self, val: bool):
        self.__bit_buf.put_bits([val])

    def put_byte(self, byte: int, repeat: int = 1):
        for _ in range(repeat):
            converted_byte = int.to_bytes(byte, 1, 'big')
            self.__bit_buf.put_bytes(converted_byte)

    def get_data(self):
        return self.__bit_buf.finalise()


class ByteDecoder:
    def __init__(self, data: bytes):
        self.__buf = bit_encoder.BitDecoder(data)

    def has_more(self):
        return self.__buf.has_more()

    def consume_bytes(self, length: int):
        self.__buf.advance_bytes(length)

    def peek(self, length: int):
        return self.__buf.as_bytes()[:length]

    def get_string(self):
        length = _string_len(self.__buf.as_bytes())
        string = self.__buf.as_bytes()[0:length]
        self.__buf.advance_bytes(length + 1)

        return string.decode('ascii')

    def get_int(self, length: int):
        number = int.from_bytes(self.__buf.as_bytes()[0:length], 'big')
        self.__buf.advance_bytes(length)

        return number

    def get_bool(self):
        val = self.__buf.as_bit_list()[0]
        self.__buf.advance_bits(1)
        return val

    def get_byte(self):
        b = self.__buf.as_bytes()[0]
        self.__buf.advance_bytes(1)
        return b
