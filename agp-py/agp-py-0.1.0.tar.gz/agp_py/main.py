from dataclasses import dataclass
from .models.mappings import *
from .assets.traits import traits
from .assets.parts import parts


@dataclass
class AxieGene:
    def __init__(self, hex_string: str, hex_type: int = 256):
        self.hex_size = hex_type

        if self.hex_size != 256 and self.hex_size != 512:
            raise ValueError("AxieGene hex_type needs to be 256 or 512!")

        self.bin_hex: str = self.hex_to_binary(hex_string)
        self.bin_dict: dict = self.format_binary_data(self.bin_hex)
        self.genes: dict = self.axie_gene_from_binary(self.bin_dict)

    @staticmethod
    def hex_to_binary(hex_string: str) -> str:
        """
        Turns the Hex to Binary
        :param hex_string: str
        :return: str
        """
        hex_string = hex_string[2:]
        try:
            decoded_hex = "{0:04b}".format(int(hex_string, 16)).zfill(256)
        except ValueError:
            raise ValueError("Cannot turn this string into binary")

        return decoded_hex

    def format_binary_data(self, bin_data: str) -> dict:
        """
        Slices the Binary input into a dictionary to organize the axie parts
        :param bin_data: str
        :return: dict
        """
        return {
            "cls": bin_data[0:4] if self.hex_size == 256 else bin_data[0:5],
            "region": bin_data[8:13] if self.hex_size == 256 else bin_data[22:40],
            "tag": bin_data[13:18] if self.hex_size == 256 else bin_data[40:50],
            "bodySkin": bin_data[18:22] if self.hex_size == 256 else bin_data[61:65],
            "xMas": bin_data[22:34] if self.hex_size == 256 else '',
            "pattern": bin_data[34:52] if self.hex_size == 256 else bin_data[65:92],
            "color": bin_data[52:64] if self.hex_size == 256 else bin_data[92:110],
            "eyes": bin_data[64:96] if self.hex_size == 256 else bin_data[149:192],
            "mouth": bin_data[96:128] if self.hex_size == 256 else bin_data[213:256],
            "ears": bin_data[128:160] if self.hex_size == 256 else bin_data[277:320],
            "horn": bin_data[160:192] if self.hex_size == 256 else bin_data[341:384],
            "back": bin_data[192:224] if self.hex_size == 256 else bin_data[405:448],
            "tail": bin_data[224:256] if self.hex_size == 256 else bin_data[469:512],
        }

    def axie_gene_from_binary(self, bin_data: dict) -> dict:
        """
        Turns the Binary data in the dictionary to its real-world values
        :param bin_data: dict
        :return: dict
        """

        data = {
            "cls": ClassMap[bin_data["cls"]].value,
            "region": RegionMap[bin_data["region"]].value,
            "tag": TagMap[bin_data["tag"]].value,
            "bodySkin": BodySkinMap[bin_data["bodySkin"]].value,
            "pattern": self.parse_patterns(bin_data["pattern"]),
            "color": self.parse_colors(bin_data["color"], ClassMap[bin_data["cls"]]),
            "eyes": self.parse_part(bin_data["eyes"], bin_data, AxiePart.Eyes),
            "mouth": self.parse_part(bin_data["mouth"], bin_data, AxiePart.Mouth),
            "ears": self.parse_part(bin_data["ears"], bin_data, AxiePart.Ears),
            "horn": self.parse_part(bin_data["horn"], bin_data, AxiePart.Horn),
            "back": self.parse_part(bin_data["back"], bin_data, AxiePart.Back),
            "tail": self.parse_part(bin_data["tail"], bin_data, AxiePart.Tail),
        }

        return data

    @staticmethod
    def parse_colors(bin_data: str, axie_class: AxieClass) -> dict:
        """
        Turns the string into a dictionary (of axie colors) with dominant and recessive genes
        :param bin_data: str
        :param axie_class: AxieClass
        :return: dict
        """
        color_length = len(bin_data) // 3
        d, r1, r2 = [bin_data[i:i + color_length] for i in range(0, len(bin_data), color_length)]
        return {
            "d": ColorMap[axie_class][d[-4:]] if d[-4:] in ColorMap[axie_class] else d[-4:],
            "r1": ColorMap[axie_class][r1[-4:]] if r1[-4:] in ColorMap[axie_class] else r1[-4:],
            "r2": ColorMap[axie_class][r2[-4:]] if r2[-4:] in ColorMap[axie_class] else r2[-4:],
        }

    @staticmethod
    def parse_patterns(bin_data: dict) -> dict:
        """
        Turns the string into a dictionary (of axie patterns) with dominant and recessive genes
        :param bin_data: str
        :return: dict
        """
        color_length = len(bin_data) // 3
        d, r1, r2 = [bin_data[i:i + color_length] for i in range(0, len(bin_data), color_length)]

        return {"d": d, "r1": r1, "r2": r2}

    def parse_part(self, bin_part_data: dict, bin_data: dict, part_type: AxiePart):
        """
        Find what are the dominant and recessive genes for a given part
        :param bin_part_data: dict
        :param bin_data: dict
        :param part_type: AxiePart
        :return:
        """
        d_class = ClassMap[bin_part_data[2:6] if self.hex_size == 256 else bin_part_data[4:9]]
        bin_d = bin_part_data[6:12] if self.hex_size == 256 else bin_part_data[11:17]
        d = self.find_part(d_class, part_type, RegionMap[bin_data["region"]], bin_d)

        r1_class = ClassMap[bin_part_data[12:16] if self.hex_size == 256 else bin_part_data[17:22]]
        bin_r1 = bin_part_data[16:22] if self.hex_size == 256 else bin_part_data[24:30]
        r1 = self.find_part(r1_class, part_type, RegionMap[bin_data["region"]], bin_r1)

        r2_class = ClassMap[bin_part_data[22:26] if self.hex_size == 256 else bin_part_data[30:35]]
        bin_r2 = bin_part_data[26:32] if self.hex_size == 256 else bin_part_data[37:43]
        r2 = self.find_part(r2_class, part_type, RegionMap[bin_data["region"]], bin_r2)

        mystic = self.parse_skin(bin_data["region"], bin_part_data[0:2] if self.hex_size == 256 else bin_part_data[0:4]) == AxiePartSkin.Mystic

        return {"d": d, "r1": r1, "r2": r2, "mystic": mystic}

    def parse_skin(self, bin_region: str, bin_skin: str) -> PartSkinMap:
        """
        Turns the string into an Axie Skin
        :param bin_region: str
        :param bin_skin: str
        :return: str
        """
        try:
            skin = PartSkinMap[bin_skin]
        except KeyError:
            skin = None

        if bin_skin == '00' and self.bin_dict["xMas"] == '010101010101':
            skin = AxiePartSkin.Xmas1
        elif bin_skin == '00' and self.bin_dict["xMas"] != '010101010101':
            skin = PartSkinMap[bin_region]

        return skin

    @staticmethod
    def find_part(axie_class: ClassMap, part_type: AxiePart, region: RegionMap,
                  bin_part) -> dict:
        """
        Finds the correct part in a dictionary
        :param axie_class: ClassMap
        :param part_type: AxiePart
        :param region: RegionMap
        :param bin_part: dict
        :return: dict
        """
        part = traits[axie_class.value][part_type.value][bin_part][region.value]

        return parts["{}-{}".format(part_type.value, part.lower().replace(' ', '-').replace("'", ''))]
