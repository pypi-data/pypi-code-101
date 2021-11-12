import logging
from logging import StreamHandler, Formatter
import os
import sys
from unittest import TestCase

import numpy as np
from voxypy.numpy_vox_io.models import Vox

from voxypy.numpy_vox_io.parser import VoxParser
from voxypy.numpy_vox_io.writer import VoxWriter

TEST_DIR = os.path.sep.join([os.getcwd(), 'test'])
log = logging.getLogger()
log.setLevel(logging.DEBUG)
handler = StreamHandler(stream=sys.stdout)
handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s\t] %(message)s'))
log.addHandler(handler)


class TestParser(TestCase):
    def test_read_from_file(self):
        filename = os.path.sep.join([TEST_DIR, 'howdy.vox'])
        try:
            voxels, palette = VoxParser(filename).parse()
        except Exception as exc:
            self.fail(f"Failed to read from file {filename} :: {exc}")

    def test_read_write(self):
        in_filename = os.path.sep.join([TEST_DIR, 'single.vox'])
        out_filename = os.path.sep.join([TEST_DIR, 'single2.vox'])
        vox = VoxParser(in_filename)
        try:
            log.info("Parsing...")
            vox, palette = vox.parse()
            vox = Vox.from_dense(vox, palette_thru=palette)
        except Exception as exc:
            self.fail(f"Failed to read from file {in_filename} :: {exc}")

        try:
            log.info("Writing...")
            VoxWriter(out_filename, vox).write()
        except Exception as exc:
            self.fail(f"Failed to write file {out_filename} :: {exc}")

        vox2 = None
        try:
            log.info("Parsing again...")
            vox2, palette = VoxParser(out_filename).parse()
            vox2 = Vox.from_dense(vox2, palette_thru=palette)
        except Exception as exc:
            self.fail(f"Failed to read from file {out_filename} :: {exc}")

        self.assertTrue(np.array_equal(vox.to_dense(), vox2.to_dense()),
                        "Entities should be the same before and after writing.")

        try:
            os.remove(out_filename)
        except Exception as exc:
            print(f"Failed to clean up after unit test. File: {out_filename}")
        # TODO: add comparisons for materials and such.
