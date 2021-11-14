import os
from unittest import TestCase

import numpy as np

from voxypy.models import Entity, validate_and_pad_palette, Color

HOWDY_FILE = os.path.sep.join(['test', 'howdy.vox'])
RED_FILE = os.path.sep.join(["test", "red.png"])
SINGLE_FILE = os.path.sep.join(["test", "single.vox"])
SINGLE_2_FILE = os.path.sep.join(["test", "single_2.vox"])
TINY_FILE = os.path.sep.join(['test', 'tiny.vox'])

def matrices_are_equal(m1, m2):
    return all([m1[x][y] == m2[x][y] for x in range(len(m1)) for y in range(len(m1[0]))])


def print_layers(a):
    s = ""
    for row in range(a.shape[2]):
        s += str(a[:, :, row])
        s += "\n\n"
    return s


def print_slices(a):
    s = ""
    for xy_slice in range(a.shape[1]):
        s += str(a[:, xy_slice, :])
        s += "\n\n"
    return s


class TestEntity(TestCase):

    def test_str(self):
        x, y, z = 1, 2, 3
        entity = Entity(x, y, z)
        entity.set(0, 0, 0, 255)
        self.assertEqual(str(entity), "Entity with dimensions x=1, y=2, z=3")

    def test_init_dense_bad_data(self):
        try:
            data = [[[0, 0, 0], [0, 0, 0]]]
            entity = Entity(3, 2, 1, data=data)
            self.fail("Should have failed with a mismatched data type.")
        except TypeError:
            pass
        except Exception as exc:
            self.fail(f"Unexpected exception type {exc}")

    def test_init_dense_bad_shape(self):
        shape = (1, 2, 3)
        arr = np.zeros(shape, dtype=int)
        try:
            entity = Entity(*shape[::-1], data=arr)
            self.fail("Should have failed with mismatched shape.")
        except ValueError:
            pass
        except Exception as exc:
            self.fail(f"Unexpected exception type {exc}")

    def test_init_dense_bad_dtype(self):
        shape = (1, 2, 3)
        try:
            data = np.zeros(shape, dtype=float)
            entity = Entity(data=data)
            self.fail("Should have failed with a mismatched data type.")
        except TypeError:
            pass
        except Exception as exc:
            self.fail(f"Unexpected exception type {exc}")

    def test_init_dense_success(self):
        shape = (1, 2, 3)
        arr = np.zeros(shape, dtype=int)
        entity = Entity(*shape, arr)
        expected = np.zeros(shape[:2], dtype=int)
        actual = entity.get_layer(0)
        self.assertTrue(np.array_equal(expected, actual), f"Expected: {expected}\n\nActual: {actual}")
        self.assertEqual((entity.x, entity.y, entity.z), shape)

    def test_get_all_voxels(self):
        x, y, z = 2, 2, 1
        entity = Entity(x, y, z)
        expected = [0, 0, 0, 0]
        actual = [vox for vox in entity.all_voxels()]
        self.assertEqual(expected, actual)

    def test_get_set(self):
        x, y, z = 1, 2, 3
        entity = Entity(x, y, z)
        entity.set(0, 1, 2, 255)
        self.assertEqual(entity.get(0, 1, 2), 255)

    def test_equality(self):
        x, y, z = 1, 2, 3
        entity = Entity(x, y, z)
        correct_entity = Entity(x, y, z)
        self.assertTrue(entity == correct_entity, f"{entity}\nshould equal\n{correct_entity}")
        incorrect_entity = Entity(x, y, z).set(0, 0, 0, 1)
        self.assertFalse(entity == incorrect_entity, f"{entity}\nshould not equal\n{incorrect_entity}")

    def test_get_layer(self):
        x, y, z = 1, 2, 3
        entity = Entity(x, y, z)
        expected = np.zeros((1, 2), dtype=int)
        actual = entity.get_layer(0)
        self.assertEqual(len(expected), x, "X dimension is incorrect.")
        self.assertEqual(len(expected[0]), y, "Y dimension is incorrect.")
        self.assertTrue(matrices_are_equal(expected, actual), "Expected %s\n\nbut received %s" % (expected, actual))
        for _x in range(x):
            for _y in range(y):
                entity.set(_x, _y, z=1, color=255)
                expected[_x][_y] = 255
        actual = entity.get_layer(1)
        self.assertTrue(matrices_are_equal(expected, actual), "Expected %s\n\nbut received %s" % (expected, actual))

    def test_set_layer(self):
        x, y, z = 1, 2, 3
        entity = Entity(x, y, z)
        layer = np.zeros((1, 2), dtype=int)
        layer[:][:] = 255
        entity.set_layer(z=0, layer=layer)
        actual = entity.get_layer(0)
        self.assertTrue(matrices_are_equal(layer, actual), "Expected %s\n\nbut received %s" % (layer, actual))

    def test_read_from_file(self):
        filename = HOWDY_FILE
        try:
            entity = Entity().from_file(filename)
        except Exception as exc:
            self.fail(f"Failed to read from file {filename} :: {exc}")

    def test_read_write(self):
        in_filename = SINGLE_FILE
        out_filename = SINGLE_2_FILE
        entity = Entity()
        entity2 = Entity()
        try:
            entity.from_file(in_filename)
        except Exception as exc:
            self.fail(f"Failed to read from file {in_filename} :: {exc}")

        try:
            print(f"Writing {out_filename}")
            entity.write(out_filename)
        except Exception as exc:
            self.fail(f"Failed to write file {out_filename} :: {exc}")

        try:
            entity2.from_file(out_filename)
        except Exception as exc:
            self.fail(f"Failed to read from file {out_filename} :: {exc}")

        self.assertEqual(entity, entity2, f"Entities should be the same before and after writing.\n"
                                          f"Entity 1:\n{entity}\n{print_slices(entity.get_dense())}\n"
                                          f"Entity 2:\n{entity2}\n{print_slices(entity2.get_dense())}")

        try:
            os.remove(out_filename)
        except Exception as exc:
            print(f"Failed to clean up after unit test. File: {out_filename}")

    def test_init_vs_file(self):
        tiny_mem = np.zeros((1, 2, 3), dtype=int)
        i = 1

        for z in range(3):
            for y in range(2):
                for x in range(1):
                    tiny_mem[x, y, z] = i
                    i += 1
        tiny_disk = Entity().from_file(TINY_FILE).get_dense()
        self.assertTrue(np.array_equal(tiny_mem, tiny_disk), f"\nMemory:\n{print_layers(tiny_mem)}"
                                                             f"\nDisk:\n{print_layers(tiny_disk)}")

    def test_read_palette_from_vox_file(self):
        entity = Entity().from_file(SINGLE_FILE)
        expected = [Color(75, 75, 75, 255)] * 255
        self.assertEqual(expected, entity.get_palette(padded=False))

    def test_read_palette_after_import(self):
        entity = Entity().from_file(SINGLE_FILE)
        entity.set_palette_from_file(RED_FILE)
        expected = [Color(255, 0, 0, 255)] * 255
        self.assertEqual(expected, entity.get_palette(padded=False))

    def test_validate_pad_palette_works(self):
        try:
            palette = [(i, i, i, i) for i in range(255)]
            validate_and_pad_palette(palette)
        except ValueError as exc:
            self.fail(f"Validation for working case failed: {exc}")

    def test_validate_pad_palette_pads(self):
        palette = [(i, i, i, i) for i in range(10)]
        validate_and_pad_palette(palette)
        self.assertEqual(255, len(palette), f"Function should return padded "
                                            f"palette with length 255 but received length {len(palette)}")

    def test_validate_pad_palette_too_long(self):
        try:
            palette = [(i, i, i, i) for i in range(257)]
            validate_and_pad_palette(palette)
            self.fail("Should have failed length check.")
        except ValueError:
            pass

    def test_validate_pad_palette_bad_data(self):
        try:
            palette = [(i, i, i, i) for i in range(255)]
            palette[0] = "invalid"
            validate_and_pad_palette(palette)
            self.fail("Should have failed bad data check.")
        except ValueError:
            pass

    def test_validate_pad_palette_bad_color(self):
        try:
            palette = [(i, i, i, i) for i in range(255)]
            palette[0] = (1, 2, 3)
            validate_and_pad_palette(palette)
            self.fail("Should have failed color length check.")
        except ValueError:
            pass

    def test_validate_pad_palette_bad_channel_data(self):
        try:
            palette = [(i, i, i, i) for i in range(255)]
            palette[0] = ("invalid", 2, 3, 255)
            validate_and_pad_palette(palette)
            self.fail("Should have failed channel data check.")
        except ValueError:
            pass

    def test_validate_pad_palette_bad_channel_low(self):
        try:
            palette = [(i, i, i, i) for i in range(255)]
            palette[0] = (-1, 2, 3, 255)
            validate_and_pad_palette(palette)
            self.fail("Should have failed channel data check.")
        except ValueError:
            pass

    def test_validate_pad_palette_bad_channel_high(self):
        try:
            palette = [(i, i, i, i) for i in range(255)]
            palette[0] = (1, 2, 256, 255)
            validate_and_pad_palette(palette)
            self.fail("Should have failed channel data check.")
        except ValueError:
            pass

    def test_nonzero(self):
        entity = Entity(data=np.ones(shape=(2, 2, 2), dtype=int))
        entity.set(0, 0, 0, 0)
        actual = entity.nonzero()
        expected = [(0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1), (1, 1, 0)]
        print(actual)
        for i in range(len(expected)):
            self.assertTrue(actual[i] in expected)
        for i in range(len(actual)):
            self.assertTrue(expected[i] in actual)
