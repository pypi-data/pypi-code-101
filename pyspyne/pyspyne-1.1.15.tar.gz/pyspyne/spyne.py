# -*- coding: utf-8 -*-

from turtle import Turtle, Screen
from math import *
import random
import math
import requests, bs4

class Element:
    def __init__(self, symbol, name, group, period, block, an, state, ec, mp, bp, density, ram, disc,
                 discrvr, ar, cr, eaf, en, ionz, enth, oxd, iso, hc):
        self.name = name
        self.symbol = symbol
        self.group = group
        self.period = period
        self.block = block
        self.atomic_number = an
        self.state = state
        self.elec_config = ec
        self.melting_point = mp
        self.boiling_point = bp
        self.density = density
        self.mass = ram
        self.discovery = disc
        self.discoverer = discrvr
        self.atomic_radius = ar
        self.covalent_radius = cr
        self.e_affinity = eaf
        self.electronegativity = en
        self.ionization = ionz
        self.enthalpy = enth
        self.oxidization = oxd
        self.isotopes = iso
        self.heat_capacity = hc
class Enthalpy:
    def __init__(self, bond, atom, enthalpy, found_in="-"):
        self.bond_type = bond
        self.atom = atom
        self.enthalpy = enthalpy
        self.found_in = found_in
class Chemical:
    def __init__(self, string):
        def convert(string):

            def has_bracks(arr):
                bracks = False
                for i in arr:
                    if i[0] == "(":
                        bracks = True
                return bracks

            caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            separated = []
            number_of_brackets = 0
            for char in string:
                if char in caps and number_of_brackets == 0:
                    try:
                        if separated[-1][-1] in numbers:
                            pass
                        else:
                            separated[-1] += "1"
                    except:
                        pass
                    separated.append(char)
                elif char == "(":
                    if number_of_brackets == 0:
                        try:
                            if separated[-1][-1] in numbers:
                                pass
                            else:
                                separated[-1] += "1"
                        except:
                            pass
                        separated.append(char)
                    else:
                        separated[-1] += char
                    number_of_brackets += 1
                elif char == ")":
                    number_of_brackets -= 1
                    separated[-1] += ")"
                else:
                    separated[-1] += char
            if separated[-1][-1] not in numbers:
                separated[-1] += "1"
            arrb = []
            for i in separated:
                letters = ""
                number = ""
                brackets = 0
                for j in i:
                    if j in numbers and brackets == 0:
                        number += j
                    elif j == "(":
                        brackets += 1
                        letters += j
                    elif j == ")":
                        brackets -= 1
                        letters += j
                    else:
                        letters += j
                for _ in range(0, int(number)):
                    arrb.append(letters)
            while has_bracks(arrb):
                stringx = ""
                for i in arrb:
                    if i[0] == "(":
                        stringx = i[1:-1]
                        break
                separated = []
                number_of_brackets = 0
                for char in stringx:
                    if char in caps and number_of_brackets == 0:
                        try:
                            if separated[-1][-1] in numbers:
                                pass
                            else:
                                separated[-1] += "1"
                        except:
                            pass
                        separated.append(char)
                    elif char == "(":
                        if number_of_brackets == 0:
                            try:
                                if separated[-1][-1] in numbers:
                                    pass
                                else:
                                    separated[-1] += "1"
                            except:
                                pass
                            separated.append(char)
                        else:
                            separated[-1] += char
                        number_of_brackets += 1
                    elif char == ")":
                        number_of_brackets -= 1
                        separated[-1] += ")"
                    else:
                        separated[-1] += char
                if separated[-1][-1] not in numbers:
                    separated[-1] += "1"
                arr1 = []
                for i in separated:
                    letters = ""
                    number = ""
                    brackets = 0
                    for j in i:
                        if j in numbers and brackets == 0:
                            number += j
                        elif j == "(":
                            brackets += 1
                            letters += j
                        elif j == ")":
                            brackets -= 1
                            letters += j
                        else:
                            letters += j
                    for _ in range(0, int(number)):
                        arr1.append(letters)
                arrb.pop(arrb.index("(" + stringx + ")"))
                for l in arr1:
                    arrb.append(l)
            atom_dic = {}
            for i in arrb:
                try:
                    atom_dic[i] += 1
                except:
                    atom_dic[i] = 1
            simplified = ""
            for i in atom_dic:
                simplified += i
                if atom_dic[i] != 1:
                    simplified += str(atom_dic[i])
            return simplified

        self.raw_string = string
        self.simplified = convert(self.raw_string)
        self.csid = None
        self.density = None
        self.boiling_point = None
        self.vpressure = None
        self.enthalpy = None
        self.refraction = None
        self.melting_point = None
        self.h_acceptors = None
        self.h_donors = None
        self.free_bonds = None

    def search(self, filter_with_molecular_formula=True, input=None):
        if filter_with_molecular_formula:
            keyword = self.simplified
        else:
            if input is None:
                raise ValueError("<input> parameter of Spyne Catalyst search() function "
                                 "should not be null when <filter_with_molecular_formula> is False")
            else:
                keyword = input
        search_link = "http://www.chemspider.com/search.aspx"
        response = requests.get(search_link, params={
            "q": str(keyword)
        }).text
        search_soup = bs4.BeautifulSoup(response, "html.parser")
        csid_list = search_soup.select("div#result div.results-wrapper tbody td.search-id-column a")
        csids = [csid_xx.text.replace(" ", "").replace("\n", "") for csid_xx in csid_list]
        self.csid = int(csids[0])

        properties_link = f"http://www.chemspider.com/chemical-structure.{self.csid}.html"
        response = requests.get(properties_link).text
        prop_soup = bs4.BeautifulSoup(response, "html.parser")
        props_bef = prop_soup.select("div.info-tabs div#pred_ib_ph div.tab-content "
                                     "div.AspNet-FormView div.AspNet-FormView-Data table tr "
                                     "td.prop_title")
        values_bef = prop_soup.select("div.info-tabs div#pred_ib_ph div.tab-content "
                                      "div.AspNet-FormView div.AspNet-FormView-Data table tr "
                                      "td.prop_value_nowrap")
        props = [i.text.replace(" ", "").replace("\r", "").replace("\n", "")[0:-1] for i in props_bef]
        values = [i.text.replace(" ", "").replace("\r", "").replace("\n", "") for i in values_bef]
        self.density = float(values[props.index("Density")].split("±")[0])
        self.boiling_point = float(values[props.index("BoilingPoint")].split("±")[0])
        self.vpressure = float(values[props.index("VapourPressure")].split("±")[0])
        self.enthalpy = float(values[props.index("EnthalpyofVaporization")].split("±")[0])
        self.refraction = float(values[props.index("IndexofRefraction")])
        self.h_acceptors = int(values[props.index("#Hbondacceptors")])
        self.h_donors = int(values[props.index("#Hbonddonors")])
        self.free_bonds = int(values[props.index("#FreelyRotatingBonds")])
class Isotope:
    def __init__(self, protons, mass_number, mass, abundance=None, halflife=None, decay=None, name=None):
        self.atom = protons
        self.mass_num = mass_number
        self.mass = mass
        self.abundance = abundance
        self.half_life = halflife
        self.mode_of_decay = decay
        self.name = name
class Decay:
    def __init__(self, method):
        valids = ["alpha", "beta", "gamma"]
        if method in valids:
            self.method = method
        else:
            self.method = method[:-1]
        if self.method == "alpha":
            self.p_omit = -2
            self.n_omit = -2
            self.e_omit = 0
        elif self.method == "beta":
            self.p_omit = -1
            self.n_omit = 0
            self.e_omit = 1
        elif self.method == "gamma":
            self.p_omit = 0
            self.n_omit = 0
            self.e_omit = 0
class ElectronConfig:
    def __init__(self, string):
        ec_parts = string.split(" ")
class Kinematics:
    def __init__(self, v0, vf, a, t, x):
        self.v0 = v0
        self.vf = vf
        self.a = a
        self.t = t
        self.x = x


class Spyne:
    def __init__(self):
        # self.broccoli = Broccoli()
        self.catalyst = self.Catalyst()
        self.graphr = self.Graphr()
        self.lingo = self.Lingo()
        self.photon = self.Photon()
        self.quantum = self.Quantum()
        self.math = self.Math()

    class Catalyst:
        def __init__(self):
            self.hydrogen = Element(
                name="Hydrogen",
                symbol="H",
                group=1,
                period=1,
                block="s",
                an=1,
                state="gas",
                ec=ElectronConfig("1s1"),
                mp=13.99,
                bp=20.271,
                density=0.000082,
                ram=1.008,
                disc=1766,
                discrvr=["Henry Cavendish"],
                ar=1.1,
                cr=0.32,
                eaf=72.769,
                en=2.2,
                ionz=[1312.05],
                enth=[],
                oxd=[1, -1],
                iso=[
                    Isotope(protons=1, mass_number=2, mass=2.014, abundance=0.0115, name="Deuterium"),
                    Isotope(protons=1, mass_number=3, mass=3.016, halflife=387892800,
                                           decay=Decay("beta-"))
                ],
                hc=14304
            )
            self.helium = Element(
                name="Helium",
                symbol="He",
                group=18,
                period=1,
                block="s",
                an=2,
                state="gas",
                ec=ElectronConfig("1s2"),
                mp=0.95,
                bp=4.222,
                density=0.000164,
                ram=4.003,
                disc=1895,
                discrvr=["Sir William Ramsay"],
                ar=1.4,
                cr=0.37,
                eaf=None,
                en=None,
                ionz=[2372.322, 5250.516],
                enth=[],
                oxd=[],
                iso=[
                    Isotope(protons=2, mass_number=3, mass=3.016, abundance=0.000134),
                    Isotope(protons=2, mass_number=4, mass=4.003, abundance=99.9999)
                ],
                hc=5193
            )
            self.lithium = Element(
                name="Lithium",
                symbol="Li",
                group=1,
                period=2,
                block="s",
                an=3,
                state="solid",
                ec=ElectronConfig("2s1"),
                mp=453.65,
                bp=1615,
                density=0.534,
                ram=6.94,
                disc=1817,
                discrvr=["Johan August Arfvedson"],
                ar=1.82,
                cr=1.3,
                eaf=59.633,
                en=0.98,
                ionz=[520.222, 7298.15, 11815.044],
                enth=[],
                oxd=[1],
                iso=[
                    Isotope(protons=3, mass_number=6, mass=6.015, abundance=7.59),
                    Isotope(protons=3, mass_number=7, mass=7.016, abundance=92.41)
                ],
                hc=3582
            )
            self.beryllium = Element(
                name="Beryllium",
                symbol="Be",
                group=2,
                period=2,
                block="s",
                an=4,
                state="solid",
                ec=ElectronConfig("2s2"),
                mp=1560,
                bp=2741,
                density=1.85,
                ram=9.012,
                disc=1797,
                discrvr=["Nicholas Louis Vauquelin"],
                ar=1.53,
                cr=0.99,
                eaf=None,
                en=1.57,
                ionz=[899.504, 1757.108, 14848.767, 21006.658],
                enth=[],
                oxd=[2],
                iso=[
                    Isotope(protons=4, mass_number=9, mass=9.012, abundance=100)
                ],
                hc=1825
            )
            self.boron = Element(
                name="Boron",
                symbol="B",
                group=13,
                period=2,
                block="p",
                an=5,
                state="solid",
                ec=ElectronConfig("2s2 2p1"),
                mp=2350,
                bp=4273,
                density=2.34,
                ram=10.81,
                disc=1808,
                discrvr=["Louis-Josef Gay-Lussac", "Louis-Jacques Thénard", "Humphry Davy"],
                ar=1.92,
                cr=0.84,
                eaf=26.989,
                en=2.04,
                ionz=[800.637, 2427.069, 3659.751, 25025.905, 32826.802],
                enth=[],
                oxd=[3],
                iso=[
                    Isotope(protons=5, mass_number=9, mass=10.013, abundance=19.9),
                    Isotope(protons=5, mass_number=10, mass=11.009, abundance=80.1)
                ],
                hc=1026
            )
            self.carbon = Element(
                name="Carbon",
                symbol="C",
                group=14,
                period=2,
                block="p",
                an=6,
                state="solid",
                ec=ElectronConfig("2s2 2p2"),
                mp=4098,
                bp=4098,
                density=2.2,
                ram=12.011,
                disc=None,
                discrvr=[],
                ar=1.70,
                cr=0.75,
                eaf=121.776,
                en=2.55,
                ionz=[1086.454, 2352.631, 4620.471, 6222.716, 37830.648, 47277.174],
                enth=[],
                oxd=[3],
                iso=[
                    Isotope(protons=5, mass_number=9, mass=10.013, abundance=19.9),
                    Isotope(protons=5, mass_number=10, mass=11.009, abundance=80.1)
                ],
                hc=1026
            )
            self.nitrogen = Element(
                name="Nitrogen",
                symbol="N",
                group=15,
                period=2,
                block="p",
                an=7,
                state="gas",
                ec=ElectronConfig("2s2 2p3"),
                mp=63.2,
                bp=77.355,
                density=0.001145,
                ram=14.007,
                disc=1772,
                discrvr=["Daniel Rutherford"],
                ar=1.55,
                cr=0.71,
                eaf=None,
                en=3.04,
                ionz=[1402.328, 2856.092, 4578.156, 7475.057, 9444.969, 53266.835, 64360.16],
                enth=[],
                oxd=[-3, 5, 4, 3, 2],
                iso=[
                    Isotope(protons=7, mass_number=14, mass=14.003, abundance=99.636),
                    Isotope(protons=7, mass_number=15, mass=15, abundance=0.364)
                ],
                hc=1040
            )
            self.oxygen = Element(
                name="Oxygen",
                symbol="O",
                group=16,
                period=2,
                block="p",
                an=8,
                state="gas",
                ec=ElectronConfig("2s2 2p4"),
                mp=54.36,
                bp=90.188,
                density=0.001308,
                ram=15.999,
                disc=1774,
                discrvr=["Joseph Priestley"],
                ar=1.52,
                cr=0.64,
                eaf=140.976,
                en=3.44,
                ionz=[1313.942, 3388.671, 5300.47, 7469.271, 10989.584, 53266.835, 13326.526, 71330.65, 84078.3],
                enth=[],
                oxd=[-2, -1],
                iso=[
                    Isotope(protons=8, mass_number=16, mass=15.995, abundance=99.757),
                    Isotope(protons=8, mass_number=17, mass=16.999, abundance=0.038),
                    Isotope(protons=8, mass_number=18, mass=17.999, abundance=0.205)
                ],
                hc=918
            )
            self.fluorine = Element(
                name="Fluorine",
                symbol="F",
                group=17,
                period=2,
                block="p",
                an=9,
                state="gas",
                ec=ElectronConfig("2s2 2p5"),
                mp=53.48,
                bp=85.04,
                density=0.001553,
                ram=18.998,
                disc=1886,
                discrvr=["Henry Moissan"],
                ar=1.47,
                cr=0.6,
                eaf=328.165,
                en=3.98,
                ionz=[1681.045, 3374.17, 6050.441, 8407.713, 11022.755, 15164.128, 17867.734, 92038.447],
                enth=[],
                oxd=[-2, -1],
                iso=[
                    Isotope(protons=8, mass_number=16, mass=15.995, abundance=99.757),
                    Isotope(protons=8, mass_number=17, mass=16.999, abundance=0.038),
                    Isotope(protons=8, mass_number=18, mass=17.999, abundance=0.205)
                ],
                hc=918
            )
            self.neon = Element(
                name="Neon",
                symbol="Ne",
                group=18,
                period=2,
                block="p",
                an=10,
                state="gas",
                ec=ElectronConfig("2s2 2p6"),
                mp=24.56,
                bp=27.104,
                density=0.000825,
                ram=20.18,
                disc=1898,
                discrvr=["Sir William Ramsay", "Morris Travers"],
                ar=1.54,
                cr=0.62,
                eaf=None,
                en=None,
                ionz=[2080.662, 3952.325, 6121.99, 9370.66, 12177.41, 15237.93, 19999.086, 23069.539],
                enth=[],
                oxd=[],
                iso=[
                    Isotope(protons=10, mass_number=20, mass=19.992, abundance=90.48),
                    Isotope(protons=10, mass_number=21, mass=20.994, abundance=0.27),
                    Isotope(protons=10, mass_number=22, mass=21.991, abundance=9.25)
                ],
                hc=1030
            )
            self.sodium = Element(
                name="Sodium",
                symbol="Na",
                group=1,
                period=3,
                block="s",
                an=11,
                state="solid",
                ec=ElectronConfig("3s1"),
                mp=370.944,
                bp=1156.09,
                density=0.97,
                ram=22.99,
                disc=1807,
                discrvr=["Humphry Davy"],
                ar=2.27,
                cr=1.6,
                eaf=52.867,
                en=0.93,
                ionz=[495.845, 4562.444, 6910.28, 9543.36, 13353.6, 16612.85, 20117.2, 25496.25],
                enth=[],
                oxd=[1],
                iso=[
                    Isotope(protons=11, mass_number=23, mass=22.99, abundance=100)
                ],
                hc=1228
            )
            self.magnesium = Element(
                name="Magnesium",
                symbol="Mg",
                group=2,
                period=3,
                block="s",
                an=12,
                state="solid",
                ec=ElectronConfig("3s2"),
                mp=923,
                bp=1363,
                density=1.74,
                ram=24.305,
                disc=1755,
                discrvr=["Joseph Black"],
                ar=1.73,
                cr=1.4,
                eaf=None,
                en=1.31,
                ionz=[737.75, 1450.683, 7732.692, 10542.519, 13630.48, 13630.48, 21711.13, 25661.24],
                enth=[],
                oxd=[2],
                iso=[
                    Isotope(protons=12, mass_number=24, mass=23.985, abundance=78.99),
                    Isotope(protons=12, mass_number=25, mass=24.986, abundance=10),
                    Isotope(protons=12, mass_number=26, mass=25.983, abundance=11.01)
                ],
                hc=1023
            )
            self.aluminum = Element(
                name="Aluminum",
                symbol="Al",
                group=13,
                period=3,
                block="p",
                an=13,
                state="solid",
                ec=ElectronConfig("3s2 3p1"),
                mp=933.473,
                bp=2792,
                density=2.7,
                ram=26.982,
                disc=1825,
                discrvr=["Hans Oersted"],
                ar=1.84,
                cr=1.24,
                eaf=41.762,
                en=1.61,
                ionz=[577.539, 1816.679, 2744.781, 11577.469, 14841.857, 18379.49, 23326.3, 27465.52],
                enth=[],
                oxd=[3],
                iso=[
                    Isotope(protons=13, mass_number=27, mass=26.982, abundance=100)
                ],
                hc=897
            )
            self.silicon = Element(
                name="Silicon",
                symbol="Si",
                group=14,
                period=3,
                block="p",
                an=14,
                state="solid",
                ec=ElectronConfig("3s2 3p2"),
                mp=1687,
                bp=3538,
                density=2.3296,
                ram=28.085,
                disc=1824,
                discrvr=["Jöns Jacob Berzelius"],
                ar=2.1,
                cr=1.14,
                eaf=134.068,
                en=1.9,
                ionz=[786.518, 1577.134, 3231.585, 4355.523, 16090.571, 19805.55, 23783.6, 29287.16],
                enth=[],
                oxd=[4, -4],
                iso=[
                    Isotope(protons=14, mass_number=28, mass=27.977, abundance=92.223),
                    Isotope(protons=14, mass_number=29, mass=28.976, abundance=4.685),
                    Isotope(protons=14, mass_number=30, mass=29.974, abundance=3.092)
                ],
                hc=712
            )
            self.phosphorus = Element(
                name="Phosphorus",
                symbol="P",
                group=15,
                period=3,
                block="p",
                an=15,
                state="solid",
                ec=ElectronConfig("3s2 3p3"),
                mp=317.3,
                bp=553.7,
                density=1.823,
                ram=30.974,
                disc=1669,
                discrvr=["Hennig Brandt"],
                ar=1.8,
                cr=1.09,
                eaf=72.037,
                en=2.19,
                ionz=[1011.812, 1907.467, 2914.118, 4963.582, 6273.969, 21267.395, 25430.64, 29871.9],
                enth=[],
                oxd=[5, 3, -3],
                iso=[
                    Isotope(protons=15, mass_number=31, mass=30.974, abundance=100)
                ],
                hc=769
            )
            self.sulfur = Element(
                name="Sulfur",
                symbol="S",
                group=16,
                period=3,
                block="p",
                an=16,
                state="solid",
                ec=ElectronConfig("3s2 3p4"),
                mp=388.36,
                bp=717.76,
                density=2.07,
                ram=32.06,
                disc=None,
                discrvr=[],
                ar=1.8,
                cr=1.04,
                eaf=200.41,
                en=2.58,
                ionz=[999.589, 2251.763, 3356.72, 4556.231, 7004.305, 8495.824, 27107.363, 31719.56],
                enth=[],
                oxd=[6, 4, 2, -2],
                iso=[
                    Isotope(protons=16, mass_number=32, mass=31.972, abundance=94.99),
                    Isotope(protons=16, mass_number=33, mass=32.971, abundance=0.75),
                    Isotope(protons=16, mass_number=34, mass=33.968, abundance=4.25),
                    Isotope(protons=16, mass_number=36, mass=35.967, abundance=0.01)
                ],
                hc=708
            )
            self.chlorine = Element(
                name="Chlorine",
                symbol="Cl",
                group=17,
                period=3,
                block="p",
                an=17,
                state="gas",
                ec=ElectronConfig("3s2 3p5"),
                mp=171.7,
                bp=239.11,
                density=0.002898,
                ram=35.45,
                disc=1774,
                discrvr=["Carl Willhelm Scheele"],
                ar=1.75,
                cr=1,
                eaf=348.575,
                en=3.16,
                ionz=[1251.186, 2297.663, 3821.78, 5158.608, 6541.7, 9361.97, 11018.221, 33603.91],
                enth=[],
                oxd=[-1, 7, 5, 3, 1],
                iso=[
                    Isotope(protons=17, mass_number=35, mass=34.969, abundance=75.76),
                    Isotope(protons=17, mass_number=37, mass=36.966, abundance=24.24)
                ],
                hc=479
            )
            self.argon = Element(
                name="Argon",
                symbol="Ar",
                group=18,
                period=3,
                block="p",
                an=18,
                state="gas",
                ec=ElectronConfig("3s2 3p6"),
                mp=83.81,
                bp=87.302,
                density=0.001633,
                ram=39.95,
                disc=1894,
                discrvr=["Lord Rayleigh", "Sir William Ramsay"],
                ar=1.88,
                cr=1.01,
                eaf=None,
                en=None,
                ionz=[1520.571, 2665.857, 3930.81, 5770.79, 7238.33, 8781.034, 11995.347, 13841.79],
                enth=[],
                oxd=[],
                iso=[
                    Isotope(protons=18, mass_number=36, mass=35.968, abundance=0.3336),
                    Isotope(protons=18, mass_number=38, mass=37.963, abundance=0.0629),
                    Isotope(protons=18, mass_number=40, mass=39.962, abundance=99.6035)
                ],
                hc=520
            )
            self.potassium = Element(
                name="Potassium",
                symbol="K",
                group=1,
                period=4,
                block="s",
                an=19,
                state="solid",
                ec=ElectronConfig("4s1"),
                mp=336.7,
                bp=1032,
                density=0.89,
                ram=39.098,
                disc=1807,
                discrvr=["Humphry Davy"],
                ar=1.88,
                cr=2,
                eaf=48.385,
                en=0.82,
                ionz=[418.81, 3051.83, 4419.607, 5876.92, 7975.48, 9590.6, 11342.82, 14943.65],
                enth=[],
                oxd=[1],
                iso=[
                    Isotope(protons=19, mass_number=39, mass=38.964, abundance=93.2581),
                    Isotope(protons=19, mass_number=40, mass=39.964, abundance=0.0117,
                                           halflife=1639872000000000, decay="beta"),
                    Isotope(protons=19, mass_number=41, mass=40.962, abundance=6.7302)
                ],
                hc=757
            )
            self.calcium = Element(
                name="Calcium",
                symbol="Ca",
                group=2,
                period=4,
                block="s",
                an=20,
                state="solid",
                ec=ElectronConfig("4s2"),
                mp=1115,
                bp=1757,
                density=1.54,
                ram=40.078,
                disc=1808,
                discrvr=["Humphry Davy"],
                ar=2.31,
                cr=1.74,
                eaf=2.369,
                en=1,
                ionz=[418.81, 3051.83, 4419.607, 5876.92, 7975.48, 9590.6, 11342.82, 14943.65],
                enth=[],
                oxd=[1],
                iso=[
                    Isotope(protons=19, mass_number=39, mass=38.964, abundance=93.2581),
                    Isotope(protons=19, mass_number=40, mass=39.964, abundance=0.0117,
                                           halflife=1639872000000000, decay="beta"),
                    Isotope(protons=19, mass_number=41, mass=40.962, abundance=6.7302)
                ],
                hc=757
            )
            self.elements = [self.hydrogen, self.helium, self.lithium,
                             self.beryllium, self.boron, self.carbon,
                             self.nitrogen, self.oxygen, self.fluorine,
                             self.neon, self.sodium, self.magnesium,
                             self.aluminum, self.silicon, self.phosphorus,
                             self.sulfur, self.chlorine, self.argon,
                             self.potassium]
            # enthalpies = {
            #     0: [
            #         Enthalpy(1, self.bromine, 365.7, Chemical("HBr")),
            #         Enthalpy(1, self.chlorine, 431.4, Chemical("HCl")),
            #         Enthalpy(1, self.fluorine, 565, Chemical("HF")),
            #         Enthalpy(1, self.silicon, 318, Chemical("SiH4")),
            #         Enthalpy(1, self.nitrogen, 390.8, Chemical("NH3")),
            #         Enthalpy(1, self.phosphorus, 322, Chemical("PH3")),
            #         Enthalpy(1, self.arsenic, 247, Chemical("AsH3")),
            #         Enthalpy(1, self.carbon, 413),
            #         Enthalpy(1, self.carbon, 415.5, Chemical("CH4")),
            #         Enthalpy(1, self.sulfur, 347, Chemical("H2S")),
            #         Enthalpy(1, self.iodine, 298.7, Chemical("HI")),
            #         Enthalpy(1, self.oxygen, 462.8, Chemical("H2O")),
            #         Enthalpy(1, self.selenium, 276, Chemical("H2Se"))
            #     ],
            #     5: [
            #         Enthalpy(1, self.carbon, 345.6, "-"),
            #         Enthalpy(2, self.carbon, 610, "-"),
            #         Enthalpy(3, self.carbon, 835.1, "-"),
            #         Enthalpy(1, self.nitrogen, 304.6, "-"),
            #         Enthalpy(2, self.nitrogen, 615, "-"),
            #         Enthalpy(3, self.nitrogen, 889.5, "-"),
            #         Enthalpy(1, self.fluorine, 485, "CF4"),
            #         Enthalpy(1, self.silicon, 301, "(CH3)4Si"),
            #         Enthalpy(1, self.chlorine, 339, "-"),
            #         Enthalpy(1, self.chlorine, 327.2, "CCl4"),
            #         Enthalpy(1, self.iodine, 218, "-"),
            #         Enthalpy(1, self.iodine, 213, "CH3I"),
            #         Enthalpy(1, self.bromine, 285, "-"),
            #         Enthalpy(1, self.hydrogen, 413, "-"),
            #         Enthalpy(1, self.hydrogen, 415.5, "CH4"),
            #         Enthalpy(2, self.oxygen, 357.7, "-"),
            #         Enthalpy(2, self.oxygen, 803, "CO2"),
            #         Enthalpy(2, self.oxygen, 695, "HCHO"),
            #         Enthalpy(2, self.oxygen, 736, "-aldehydes"),
            #         Enthalpy(1, self.oxygen, 749, "-ketones"),
            #         Enthalpy(1, self.oxygen, 335.6, "CH3OH")
            #     ],
            #     6: [
            #         Enthalpy(1, self.nitrogen, 163, "N2H4"),
            #         Enthalpy(2, self.nitrogen, 418, "C6H14N2"),
            #         Enthalpy(3, self.nitrogen, 944.7, "N2"),
            #         Enthalpy(1, self.carbon, 304.6, "-"),
            #         Enthalpy(2, self.carbon, 615, "-"),
            #         Enthalpy(3, self.carbon, 889.5, "-"),
            #         Enthalpy(1, self.hydrogen, 390.8, "NH3"),
            #     ],
            #     7: [
            #         Enthalpy(1, self.hydrogen, 462.8, "H2O"),
            #         Enthalpy(1, self.oxygen, 146, "H2O2"),
            #         Enthalpy(2, self.oxygen, 498.3, "O2"),
            #         Enthalpy(2, self.sulfur, 435, "SO3"),
            #         Enthalpy(1, self.silicon, 452, "SiO2"),
            #         Enthalpy(1, self.carbon, 357.7, "-"),
            #         Enthalpy(2, self.carbon, 803, "CO2"),
            #         Enthalpy(2, self.carbon, 695, "HCHO"),
            #         Enthalpy(2, self.carbon, 736, "-aldehydes"),
            #         Enthalpy(2, self.carbon, 749, "-ketones"),
            #         Enthalpy(1, self.carbon, 335.6, "CH3OH"),
            #     ],
            #     8: [
            #         Enthalpy(1, self.fluorine, 155, "F2"),
            #         Enthalpy(1, self.carbon, 485, "CF4"),
            #         Enthalpy(1, self.hydrogen, 565, "HF")
            #     ],
            #     13: [
            #         Enthalpy(1, self.silicon, 222, "Si"),
            #         Enthalpy(1, self.carbon, 301, "(CH3)4Si"),
            #         Enthalpy(1, self.hydrogen, 318, "SiH4"),
            #         Enthalpy(1, self.oxygen, 452, "SiO2")
            #     ],
            #     14: [
            #         Enthalpy(1, self.phosphorus, 201, "P4"),
            #         Enthalpy(3, self.phosphorus, 488.3, "P2"),
            #         Enthalpy(1, self.hydrogen, 322, "PH3")
            #     ],
            #     15: [
            #         Enthalpy(1, self.sulfur, 226, "S8"),
            #         Enthalpy(2, self.sulfur, 351, "S2"),
            #         Enthalpy(1, self.hydrogen, 347, "H2S"),
            #         Enthalpy(2, self.oxygen, 435, "SO3")
            #     ],
            #     16: [
            #         Enthalpy(1, self.chlorine, 242.1, "Cl2"),
            #         Enthalpy(1, self.carbon, 339, "-"),
            #         Enthalpy(1, self.carbon, 327.2, "CCl4"),
            #         Enthalpy(1, self.hydrogen, 431.4, "HCl")
            #     ]
            # }

        class Chemical(Chemical):
            def __init__(self, string):
                super().__init__(string)

        class Isotope(Isotope):
            def __init__(self, protons, mass_number, mass, abundance=None, halflife=None, decay=None, name=None):
                super().__init__(protons, mass_number, mass, abundance, halflife, decay, name)

    class Graphr:
        def __init__(self):
            self.drew_grid = False
            self.eqs = []
            self.units = 0
            self.turtle = None

        def draw(self, equations, units=1):
            left = -(units * 14)
            right = (units * 14)
            c = None

            self.eqs = equations
            self.units = units

            s = Screen()
            s.setup(width=600, height=600)
            s.tracer(0)
            s.title("Spyne Graphr")

            t = Turtle()
            t.speed("fastest")
            t.hideturtle()
            t.penup()

            t.clear()

            if not self.drew_grid:
                t.clear()
                t.goto(0, 280)
                t.pendown()
                t.color("darkblue")
                t.goto(0, -280)
                t.penup()
                t.goto(-280, 0)
                t.pendown()
                t.goto(280, 0)
                c = right - units
                counter = 260
                while c != left:
                    t.penup()
                    t.goto(-5, counter)
                    t.pendown()
                    t.goto(5, counter)
                    t.penup()
                    t.goto(10, counter - 5)
                    t.write(c, align="left", font=("Arial", 10, "bold"))
                    c -= units
                    counter -= 20
                c = left + units
                counter = -260
                while c != right:
                    t.penup()
                    t.goto(counter, 5)
                    t.pendown()
                    t.goto(counter, -5)
                    t.penup()
                    t.goto(counter - 5, -15)
                    if c != 0:
                        t.write(c, align="left", font=("Arial", 10, "bold"))
                    c += units
                    counter += 20
                self.drew_grid = True
            s.update()

            t.pensize(3)
            for equation in self.eqs:
                new_equation = equation
                current_x = left
                t.penup()
                random_color = "#"
                for _ in range(0, 6):
                    random_color += str(random.randint(0, 9))
                t.color(random_color)
                while current_x < right + 0.1:
                    try:
                        x = current_x
                        y = eval(new_equation.eq)
                        coordinates = (current_x * (20 / units), y * (20 / units))
                        t.goto(coordinates)
                        t.pendown()
                    except:
                        pass
                    finally:
                        current_x += 0.1
                s.update()

            self.turtle = t

            s.exitonclick()

    class Math:
        def __init__(self):
            super().__init__()

        class Equation:
            def __init__(self, equation):
                self.eq = str(equation)

            def calculate(self, x_value):
                x = x_value
                y = eval(self.eq)
                print(x, y)
                return x, y

    class Quantum:
        def __init__(self):
            pass

        def overlap(self, arr1, arr2, items=False):
            item = []
            for v in arr1:
                for w in arr2:
                    if v == w:
                        if items:
                            item.append({
                                "item": v,
                                "index1": arr1.index(v),
                                "index2": arr2.index(w)
                            })
                        else:
                            return True
            if items:
                return item
            else:
                return False

    class Lingo:
        def __init__(self):
            pass

        def translate(self, lang_from, lang_to, input, include=False):
            link = "https://translate.google.com/"
            params = {
                "sl": lang_from.code,
                "tl": lang_to.code,
                "text": input,
                "op": "translate"
            }
            response = requests.get(url=link, params=params).text
            soup = bs4.BeautifulSoup(response, "html.parser")
            translation = soup.select("div.J0lOec span")
            t = [i.text + "\n" for i in translation]
            print(t)

        #      div.ccvoYb div.AxqVh div.OPPzxe c-wiz.P6w8m div.dePhmb div.eyKpYb div.J0lOec span.VIiyi span.JLqJ4b span
        class Language:
            def __init__(self, name):
                def valid_code(string, langs):
                    is_there = False
                    it = ""
                    for v in langs:
                        if string == langs[v]:
                            is_there = True
                            it = v
                    return is_there, it

                name = name.lower().replace(" ", "")
                languages = {
                    "afrikaans": "af",
                    "albanian": "sq",
                    "amharic": "am",
                    "arabic": "ar",
                    "armenian": "hy",
                    "azerbaijani": "az",
                    "basque": "eu",
                    "belarusian": "be",
                    "bengali": "bn",
                    "bosnian": "bs",
                    "bulgarian": "bg",
                    "catalan": "ca",
                    "cebuano": "ceb",
                    "chichewa": "ny",
                    "chinese": "zh-CN",
                    "chinese-simplified": "zh-CN",
                    "chinese-traditional": "zh-TW",
                    "corsican": "co",
                    "croatian": "hr",
                    "czech": "cs",
                    "danish": "da",
                    "dutch": "nl",
                    "english": "en",
                    "esperanto": "eo",
                    "estonian": "et",
                    "filipino": "tl",
                    "finnish": "fi",
                    "french": "fr",
                    "frisian": "fy",
                    "galician": "gl",
                    "georgian": "ka",
                    "german": "de",
                    "greek": "el",
                    "gujarati": "gu",
                    "haitiancreole": "ht",
                    "hausa": "ha",
                    "hawaiian": "haw",
                    "hebrew": "iw",
                    "hindi": "hi",
                    "hmong": "hmn",
                    "hungarian": "hu",
                    "icelandic": "is",
                    "igbo": "ig",
                    "indonesian": "id",
                    "irish": "ga",
                    "italic": "it",
                    "japanese": "ja",
                    "javanese": "jw",
                    "kannada": "kn",
                    "kazakh": "kk",
                    "khmer": "km",
                    "kinyarwanda": "rw",
                    "korean": "ko",
                    "kurdish": "ku",
                    "kurmanji": "ku",
                    "kyrgyz": "ky",
                    "lao": "lo",
                    "latin": "la",
                    "latvian": "lv",
                    "lithuanian": "lt",
                    "luxembourgish": "lb",
                    "macedonian": "mk",
                    "malagasy": "mg",
                    "malay": "ms",
                    "malayalam": "ml",
                    "maltese": "mt",
                    "maori": "mi",
                    "marathi": "mr",
                    "mongolian": "mn",
                    "myanmar": "my",
                    "burmese": "my",
                    "nepali": "ne",
                    "norwegian": "no",
                    "odia": "or",
                    "oriya": "or",
                    "pashto": "ps",
                    "persian": "fa",
                    "polish": "pl",
                    "portuguese": "pt",
                    "punjabi": "pa",
                    "romanian": "ro",
                    "russian": "ru",
                    "samoan": "sm",
                    "scotsgaelic": "gd",
                    "gaelic": "gd",
                    "serbian": "sr",
                    "sesotho": "st",
                    "shona": "sn",
                    "sindhi": "sd",
                    "sinhala": "si",
                    "slovak": "sk",
                    "slovenian": "sl",
                    "somali": "so",
                    "spanish": "es",
                    "sundanese": "su",
                    "swahili": "sw",
                    "swedish": "sv",
                    "tajik": "tg",
                    "tamil": "ta",
                    "tatar": "tt",
                    "telugu": "te",
                    "thai": "th",
                    "turkish": "tu",
                    "turkmen": "tk",
                    "ukranian": "uk",
                    "urdu": "ur",
                    "uyghur": "ug",
                    "uzbek": "uz",
                    "vietnamese": "vi",
                    "welsh": "cy",
                    "xhosa": "xh",
                    "yiddish": "yi",
                    "yoruba": "yo",
                    "zulu": "zu"
                }
                if valid_code(name, languages)[0]:
                    self.code = name
                    self.name = valid_code(name, languages)[1]
                else:
                    try:
                        self.code = languages[name]
                    except:
                        self.code = None
                        self.name = None
                        raise AttributeError("Invalid language")
                    else:
                        self.name = name

        class TranslationResult:
            def __init__(self, f, t, p, translated, ot=None):
                self.lang_from = f
                self.lang_to = t
                self.input = p
                self.output = translated
                self.other_translations = ot

    class Photon:
        def __init__(self):
            self.c = 299792458

        def kinematics(self, v0, vf=None, a=None, t=None, x=None):
            answer = {}
            if x is None:
                if vf is None:
                    x = v0 * t + 0.5 * a * t * t
                    vf = self.math.sqrt(v0 * v0 + 2 * a * x)
                else:
                    x = t * ((vf + v0) / 2)
                    a = (vf - v0) / t
                answer = Kinematics(v0, vf, a, t, x)
            elif vf is None:
                if x is None:
                    x = v0 * t + 0.5 * a * t * t
                    vf = self.math.sqrt(v0 * v0 + 2 * a * x)


