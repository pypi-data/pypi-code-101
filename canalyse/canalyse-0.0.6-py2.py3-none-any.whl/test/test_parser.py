import unittest
import os
import pandas as pd
from pandas._testing import assert_frame_equal
from canalyse.parser import (
    BiovoronoiVolumeFormatter,
    ConductivityParser,
    ConductivityFormatter,
    BiovoronoiVolumeParser,
    VldpVolumeFormatter,
    VldpVolumeParser,
)


class TestConductivityParser(unittest.TestCase):
    def setUp(self) -> None:
        self.conductivity_file = (
            f"{os.path.dirname(os.path.abspath(__file__))}/assets/conductivity.dot"
        )
        return super().setUp()

    def test_conductivity_parser(self):
        parser = ConductivityParser()

        df = parser.run(self.conductivity_file)
        # Has header expected
        reference_header = ["source", "target", "conductivity"]
        assert all(df.columns == reference_header)

    def test_conductivity_formatter(self):
        parser = ConductivityParser()
        df = parser.run(self.conductivity_file)
        formatter = ConductivityFormatter()
        new_df = formatter.run(df)
        reference_df = pd.DataFrame(
            {
                "source": ["00001_MET", "00001_MET", "00001_MET"],
                "target": ["00036_PHE", "00005_GLU", "00004_ASP"],
                "conductivity": [
                    float(0.0174476321812),
                    float(0.0214987056692),
                    float(0.0124389690164),
                ],
                "source_residue_number": [1, 1, 1],
                "source_residue_name": ["MET", "MET", "MET"],
                "target_residue_number": [36, 5, 4],
                "target_residue_name": ["PHE", "GLU", "ASP"],
            }
        )
        assert_frame_equal(new_df, reference_df)


class TestVolumeParser(unittest.TestCase):
    def setUp(self) -> None:
        self.biovoronoi_file = "{}/assets/volume_by_biovoronoi.csv".format(
            os.path.dirname(os.path.abspath(__file__))
        )
        self.truncated_biovoronoi_file = (
            "{}/assets/truncated_residue_volume_by_biovoronoi.csv".format(
                os.path.dirname(os.path.abspath(__file__))
            )
        )
        self.vldp_file = (
            f"{os.path.dirname(os.path.abspath(__file__))}/assets/volume_by_vldp.dat"
        )
        return super().setUp()

    def test_biovoronoi_parser(self):
        parser = BiovoronoiVolumeParser()
        df = parser.run(self.truncated_biovoronoi_file)
        excepted = pd.DataFrame(
            {
                "residue_number": [int(1), int(2), int(3)],
                "residue_name": ["MET", "LEU", "SER"],
                "atom_serial_number": [190, 551, 484],
                "volume": [189.451013, 172.836974, 95.910340],
            }
        )
        assert_frame_equal(excepted, df)

    def test_biovoronoi_volume_formatter(self):
        parser = BiovoronoiVolumeParser()
        df = parser.run(self.truncated_biovoronoi_file)

        formatter = BiovoronoiVolumeFormatter()
        formatted_df = formatter.run(df)

        expected = pd.DataFrame(
            {
                "residue_number": [int(1), int(2), int(3)],
                "residue_name": ["MET", "LEU", "SER"],
                "volume": [189.451013, 172.836974, 95.910340],
            }
        )

        assert_frame_equal(expected, formatted_df)

    def test_vldp_volume_parser(self):
        parser = VldpVolumeParser()
        df = parser.run(self.vldp_file)
        excepted = pd.DataFrame(
            {
                "MOL": [
                    "MET",
                    "MET",
                    "MET",
                    "MET",
                    "MET",
                    "MET",
                    "MET",
                    "MET",
                    "LEU",
                    "LEU",
                    "LEU",
                    "LEU",
                    "LEU",
                    "LEU",
                    "LEU",
                    "LEU",
                    "SER",
                    "SER",
                    "SER",
                    "SER",
                    "SER",
                    "SER",
                ],
                "NUMMOL": [
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(2),
                    int(2),
                    int(2),
                    int(2),
                    int(2),
                    int(2),
                    int(2),
                    int(2),
                    int(3),
                    int(3),
                    int(3),
                    int(3),
                    int(3),
                    int(3),
                ],
                "ATM": [
                    "N",
                    "C",
                    "C",
                    "C",
                    "S",
                    "C",
                    "C",
                    "O",
                    "N",
                    "C",
                    "C",
                    "C",
                    "C",
                    "C",
                    "C",
                    "O",
                    "N",
                    "C",
                    "C",
                    "O",
                    "C",
                    "O",
                ],
                "NUMATM": [
                    int(1),
                    int(2),
                    int(3),
                    int(4),
                    int(5),
                    int(6),
                    int(7),
                    int(8),
                    int(9),
                    int(10),
                    int(11),
                    int(12),
                    int(13),
                    int(14),
                    int(15),
                    int(16),
                    int(17),
                    int(18),
                    int(19),
                    int(20),
                    int(21),
                    int(22),
                ],
                "X": [
                    float(10.535),
                    float(10.562),
                    float(9.575),
                    float(9.389),
                    float(8.457),
                    float(8.698),
                    float(11.999),
                    float(12.404),
                    float(12.834),
                    float(14.067),
                    float(13.753),
                    float(12.650),
                    float(12.456),
                    float(13.123),
                    float(15.167),
                    float(16.090),
                    float(15.078),
                    float(15.867),
                    float(14.928),
                    float(14.540),
                    float(17.009),
                    float(16.972),
                ],
                "Y": [
                    float(16.309),
                    float(15.758),
                    float(14.579),
                    float(14.068),
                    float(15.342),
                    float(14.933),
                    float(15.276),
                    float(14.191),
                    float(16.070),
                    float(15.655),
                    float(14.665),
                    float(15.020),
                    float(13.876),
                    float(16.097),
                    float(15.166),
                    float(14.465),
                    float(15.493),
                    float(14.923),
                    float(14.581),
                    float(15.752),
                    float(15.894),
                    float(17.102),
                ],
                "Z": [
                    float(18.894),
                    float(20.249),
                    float(20.461),
                    float(21.901),
                    float(22.880),
                    float(24.644),
                    float(20.556),
                    float(20.224),
                    float(21.286),
                    float(22.003),
                    float(23.154),
                    float(24.168),
                    float(25.148),
                    float(25.084),
                    float(21.035),
                    float(21.444),
                    float(19.735),
                    float(18.643),
                    float(17.425),
                    float(16.870),
                    float(18.298),
                    float(18.656),
                ],
                "AREA": [
                    float(34.0589623),
                    float(36.4225883),
                    float(40.1477033),
                    float(43.8646129),
                    float(49.3348796),
                    float(54.4717622),
                    float(37.9643616),
                    float(32.0836781),
                    float(26.1519462),
                    float(39.7680542),
                    float(42.9207456),
                    float(34.6758694),
                    float(49.1011981),
                    float(51.7178463),
                    float(41.4714871),
                    float(37.9007803),
                    float(24.0266465),
                    float(37.2295086),
                    float(45.3985222),
                    float(30.8462576),
                    float(42.6741885),
                    float(36.0355588),
                ],
                "VOLUME": [
                    float(14.6590707),
                    float(14.5675425),
                    float(18.6519289),
                    float(21.0056268),
                    float(25.2591029),
                    float(31.1341724),
                    float(15.3642868),
                    float(12.4726128),
                    float(8.10684567),
                    float(16.0408674),
                    float(19.7876417),
                    float(13.3573583),
                    float(25.8055044),
                    float(28.6529642),
                    float(17.3632058),
                    float(16.1906323),
                    float(6.92561677),
                    float(14.3182871),
                    float(23.0826519),
                    float(12.0728403),
                    float(17.7067254),
                    float(14.5538595),
                ],
                "LOCUS": [
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                    int(1),
                ],
            }
        )
        assert_frame_equal(excepted, df)

    def test_vldp_volume_formatter(self):
        parser = VldpVolumeParser()
        df = parser.run(self.vldp_file)
        formatter = VldpVolumeFormatter()
        formatted_df = formatter.run(df)

        expected_header = ["residue_number", "residue_name", "volume"]
        is_ok = set(expected_header) == set(formatted_df.columns)
        self.assertTrue(is_ok)
