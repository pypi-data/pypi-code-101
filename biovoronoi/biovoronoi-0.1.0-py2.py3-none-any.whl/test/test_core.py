import unittest

import pandas as pd
from biovoronoi.core import Core
from Bio.PDB import PDBParser
import os
import numpy as np
from numpy import float64, testing

np.set_printoptions(precision=20, floatmode="maxprec")


class TestCoreVolonoi(unittest.TestCase):
    def setUp(self) -> None:
        self.truncated_pdb_file = (
            f"{os.path.dirname(os.path.abspath(__file__))}/assets/truncated.pdb"
        )
        self.include_water_pdb_file = "{}/assets/hp36_include_water.pdb".format(
            os.path.dirname(os.path.abspath(__file__))
        )
        self.truncated_structure = PDBParser(QUIET=True).get_structure(
            "truncated_test_structure", self.truncated_pdb_file
        )
        self.include_water_structure = PDBParser(QUIET=True).get_structure(
            "hp36_include_water", self.include_water_pdb_file
        )
        return super().setUp()

    def test_calculate_voronoi_obejct(self):
        core = Core()
        core.set_structure(self.truncated_structure)
        core.calculate_voronoi_obejct()
        voronoi_vertices = core.get_voronoi_vertices()
        expected = np.array(
            [
                [20.083591527920003, -49.187222239880654, 73.64156970524279],
                [16.748381058306812, -19.37794247062628, 38.90762708302323],
                [19.07549039679916, -16.035323366514277, 51.20465567003689],
                [14.810939125071465, -21.040787956409535, 50.80841511042706],
                [22.68843762195727, -23.1167330307925, 46.631207728922604],
                [17.477526831106047, -19.442169994137387, 42.0146013789674],
                [19.174695872938084, -18.686166792615857, 49.85415376889441],
                [16.650203346892955, -20.489580604851607, 50.805020476105746],
                [19.35258355322934, -15.253966045124459, 51.8469433393359],
                [18.837707342428637, -14.428678526405742, 54.40450125143823],
                [18.304211112831762, -16.16710294091249, 52.78234445697005],
                [18.1718947507425, -16.3700075058658, 52.97544766911969],
                [18.11898859749951, -15.064510662615161, 55.02958759789155],
                [18.099873360047575, -15.09978883759952, 55.048979647699404],
                [15.990686266239742, -18.78588550448143, 51.93412834812853],
                [17.598881716671805, -14.606876895361012, 55.93556505560459],
                [17.623284198107875, -15.005891892774361, 55.79229098509168],
                [6.728397410917875, -23.27469121388116, 37.525456709419196],
                [13.096785854741912, -21.206263396564772, 46.98326889668296],
                [12.470849063612746, -20.9905313301695, 42.550588113154625],
                [18.367986522954602, -18.7024652268746, 51.55659554731588],
                [18.724826724179202, -19.041503713811085, 50.65459536044768],
                [17.771504930433647, -19.72487048401323, 51.057239852454195],
                [19.958999446431314, -20.50525749442718, 51.53202169023216],
                [19.83054809167109, -20.583072754762593, 54.60049929494329],
                [18.51380459540539, -19.144423432309964, 55.35347366854247],
                [19.560487563602038, -22.419727847282605, 52.67042539306758],
                [17.18760008948286, -20.95522165537354, 51.787346918463136],
                [18.347091176566497, -27.579237355356224, 59.49162108646448],
                [12.433451571974405, -32.9894379841473, 68.44297520978455],
                [19.93665400242038, -20.462851206427736, 54.50424649412202],
                [20.487356751271495, -18.234199825202733, 53.762933552941995],
                [20.610311711030946, -18.145027975525622, 51.29049073036211],
                [20.298055684099097, -19.673085122708105, 50.217477894870505],
                [20.695940952229975, -20.126505588740027, 50.009179045563656],
                [20.097772250775286, -20.352060168830874, 51.230175857044316],
                [21.65209911331341, -19.068356111991264, 53.63824553246089],
                [22.453622799192573, -19.56714232472314, 52.50834764329786],
                [22.852068864974317, -22.33034992692267, 55.30853228767671],
                [24.065106183479802, -21.2639983705502, 53.57869067751894],
                [23.589652547740393, 12.655638608667662, 61.58090753338824],
                [21.86829111306811, -19.78886071413719, 53.76225592930334],
                [21.79944339260274, -19.40499595913154, 53.68259444533161],
                [21.98895619314848, -19.74554520001514, 53.64451868941286],
                [21.861951802201443, -13.692803712968665, 54.59491978263922],
                [19.54089147755365, -14.548271478031179, 51.90885854881499],
                [23.233801331355775, -19.68008986523919, 51.49328623581107],
                [22.19652108540091, -7.1040824261575874, 55.669400626440805],
                [36.16168337780925, -26.68714819644426, 45.78590171886257],
                [24.312893036617464, 12.999217307599782, 60.48720943039531],
                [24.711547190063786, -1.1267954848032744, 56.83088699868688],
                [22.114618985006423, -19.651462918025317, 50.639376264749295],
                [21.332619149864648, -18.655437603968164, 51.117600239010066],
                [22.517693074479777, -19.52413084456844, 51.26792939364684],
                [21.193782787313832, -4.569662664489329, 56.19821216923597],
                [22.529539253724593, 3.008226096079742, 58.19796681032273],
                [22.013233317298223, -6.2063009705852075, 55.92447660368581],
            ],
            dtype=float64,
        )
        testing.assert_array_equal(voronoi_vertices, expected)

    def test_calculate_voronoi_volume_without_water(self):
        core = Core()
        core.set_structure(self.truncated_structure)
        core.calculate_voronoi_obejct()
        core.calculate_voronoi_volumes()
        volumes = core.get_voronoi_volumes()

        expected = np.array(
            [
                2217.668868555809,
                72.15707488707689,
                1986.5660227368594,
                146.57551430790733,
                47.35463601695278,
                7.951857123595612,
                2012.678635919175,
                233.16042763693022,
                150.31327544655827,
                27.927088181836062,
                78.41902701036945,
                43.722018324150255,
                3938.217866436166,
                203.53393779823216,
                74.75869837187788,
                35.61488097333656,
                77.63156398167348,
                1053.3992398337455,
            ],
            dtype=np.float64,
        )
        testing.assert_array_equal(expected, volumes)

    @unittest.skip("Calculation of voronoi volume within waters takes a long time")
    def test_voronoi_volume_with_water(self):
        core = Core()
        core.set_structure(self.include_water_structure)
        core.calculate_voronoi_obejct()
        core.calculate_voronoi_volumes()
        volumes = core.get_voronoi_volumes()
        print(volumes)

    def test_create_df(self):
        core = Core()
        core.set_structure(self.truncated_structure)
        core.calculate_voronoi_obejct()
        core.calculate_voronoi_volumes()
        core.create_df()
        df = core.get_df()

        expected = pd.DataFrame(
            [
                ["CA", 1, "THR", 5, 2217.668869],
                ["C", 2, "THR", 5, 72.157075],
                ["O", 3, "THR", 5, 1986.566023],
                ["N", 4, "SER", 6, 146.575514],
                ["CA", 5, "SER", 6, 47.354636],
                ["C", 6, "SER", 6, 7.951857],
                ["O", 7, "SER", 6, 2012.678636],
                ["CB", 8, "SER", 6, 233.160428],
                ["OG", 9, "SER", 6, 150.313275],
                ["N", 10, "GLN", 7, 27.927088],
                ["CA", 11, "GLN", 7, 78.419027],
                ["C", 12, "GLN", 7, 43.722018],
                ["O", 13, "GLN", 7, 3938.217866],
                ["CB", 14, "GLN", 7, 203.533938],
                ["CG", 15, "GLN", 7, 74.758698],
                ["CD", 16, "GLN", 7, 35.614881],
                ["OE1", 17, "GLN", 7, 77.631564],
                ["NE2", 18, "GLN", 7, 1053.399240],
            ],
            columns=[
                "atom_name",
                "atom_serial_number",
                "residue_name",
                "residue_id",
                "volume",
            ],
        )
        pd.testing.assert_frame_equal(expected, df)

    @unittest.skip
    def test_create_df_with_water(self):
        core = Core()
        core.set_structure(self.include_water_structure)
        core.calculate_voronoi_obejct()
        core.calculate_voronoi_volumes()
        core.create_df()
        df = core.get_df()
        print(df.head())

    def test_create_residue_volume(self):
        core = Core()
        core.set_structure(self.truncated_structure)
        core.calculate_voronoi_obejct()
        core.calculate_voronoi_volumes()
        core.create_df()
        core.groupby_residue()
        df = core.get_residue_df()
        print(df.head())

    @unittest.skip
    def test_create_residue_volume_with_water(self):
        core = Core()
        core.set_structure(self.include_water_structure)
        core.calculate_voronoi_obejct()
        core.calculate_voronoi_volumes()
        core.create_df()
        core.groupby_residue()
        df = core.get_residue_df()
        print(df.head())
