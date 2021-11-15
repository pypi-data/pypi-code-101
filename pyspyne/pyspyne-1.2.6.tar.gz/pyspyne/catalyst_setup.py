import requests
from bs4 import BeautifulSoup


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
        search_soup = BeautifulSoup(response, "html.parser")
        csid_list = search_soup.select("div#result div.results-wrapper tbody td.search-id-column a")
        csids = [csid_xx.text.replace(" ", "").replace("\n", "") for csid_xx in csid_list]
        self.csid = int(csids[0])

        properties_link = f"http://www.chemspider.com/chemical-structure.{self.csid}.html"
        response = requests.get(properties_link).text
        prop_soup = BeautifulSoup(response, "html.parser")
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
