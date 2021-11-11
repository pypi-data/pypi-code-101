import unittest
from Bio.PDB import PDBParser
import os


class TestBioPython(unittest.TestCase):
    def test_is_enable_parser_load_water(self):
        parser = PDBParser()
        structure = parser.get_structure(
            "hp36_include_water",
            "{}/assets/hp36_include_water.pdb".format(
                os.path.dirname(os.path.abspath(__file__))
            ),
        )
        the_number_of_atoms = len(list(structure.get_atoms()))
        expected = int(7589)
        self.assertEqual(expected, the_number_of_atoms)
