import math
import random
import string
import unittest

from src.binary_encoder import BinaryEncoder, BinaryDecoder
from src.bit_encoder import BitAlignedEncoder, BitAlignedDecoder


def id_generator(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))


class TestBit(unittest.TestCase):
    def test_random(self):
        for _ in range(10000):
            bits = []
            for _ in range(random.randrange(16251)):
                bits.append(random.random() > 0.5)

            a = BitAlignedEncoder()
            a.put_bits(bits)
            result = a.finalise()

            b = BitAlignedDecoder(result)
            recovered = b.as_bit_list()

            self.assertEqual(bits, recovered)


class TestByte(unittest.TestCase):
    def test_random(self):
        funcs = ['string', 'int', 'bool', 'byte']
        for _ in range(100):
            enc = BinaryEncoder()

            ops = [random.choice(funcs) for _ in range(random.randrange(152))]
            values = []

            for op in ops:
                if op == 'string':
                    v = id_generator(math.floor(random.random()*25))
                    enc.put_string(v)
                    values.append(v)
                elif op == 'int':
                    v = math.floor(random.random()*256**4)
                    enc.put_int(v, 4)
                    values.append(v)
                elif op == 'bool':
                    v = random.random() > 0.5
                    enc.put_bool(v)
                    values.append(v)
                elif op == 'byte':
                    v = math.floor(random.random()*255)
                    enc.put_byte(v)
                    values.append(v)

            generated = enc.get_data()
            dec = BinaryDecoder(generated)

            for op in ops:
                if op == 'string':
                    v = dec.get_string()
                    self.assertEqual(v, values[0])
                    values = values[1:]
                elif op == 'int':
                    v = dec.get_int(4)
                    self.assertEqual(v, values[0])
                    values = values[1:]
                elif op == 'bool':
                    v = dec.get_bool()
                    self.assertEqual(v, values[0])
                    values = values[1:]
                elif op == 'byte':
                    v = dec.get_byte()
                    self.assertEqual(v, values[0])
                    values = values[1:]


if __name__ == '__main__':
    unittest.main()
