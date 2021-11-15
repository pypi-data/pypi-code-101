from enum import Enum


# Axie Type Mapping
class AxieClass(Enum):
    BEAST = 'beast'
    BUG = 'bug'
    BIRD = 'bird'
    PLANT = 'plant'
    AQUATIC = 'aquatic'
    REPTILE = 'reptile'
    MECH = 'mech'
    DAWN = 'dawn'
    DUSK = 'dusk'


# Axie Class Mapping
ClassMap = {
    # 256
    '0000': AxieClass.BEAST,
    '0001': AxieClass.BUG,
    '0010': AxieClass.BIRD,
    '0011': AxieClass.PLANT,
    '0100': AxieClass.AQUATIC,
    '0101': AxieClass.REPTILE,
    '1000': AxieClass.MECH,
    '1001': AxieClass.DAWN,
    '1010': AxieClass.DUSK,
    # 512
    '00000': AxieClass.BEAST,
    '00001': AxieClass.BUG,
    '00010': AxieClass.BIRD,
    '00011': AxieClass.PLANT,
    '00100': AxieClass.AQUATIC,
    '00101': AxieClass.REPTILE,
    '10000': AxieClass.MECH,
    '10001': AxieClass.DAWN,
    '10010': AxieClass.DUSK,
}

# Axie Color Mapping
ColorMap = {
    AxieClass.BEAST: {x: y for x, y in [
        ['0010', 'ffec51'],
        ['0011', 'ffa12a'],
        ['0100', 'f0c66e'],
        ['0110', '60afce'],
        ['0000', 'ffffff']
    ]
                      },

    AxieClass.BUG: {x: y for x, y in [
        ['0010', 'ff7183'],
        ['0011', 'ff6d61'],
        ['0100', 'f74e4e'],
        ['0000', 'ffffff'],
    ]},

    AxieClass.BIRD: {x: y for x, y in [
        ['0010', 'ff9ab8'],
        ['0011', 'ffb4bb'],
        ['0100', 'ff778e'],
        ['0000', 'ffffff'],
    ]},

    AxieClass.PLANT: {x: y for x, y in [
        ['0010', 'ccef5e'],
        ['0011', 'efd636'],
        ['0100', 'c5ffd9'],
        ['0000', 'ffffff'],
    ]},

    AxieClass.AQUATIC: {x: y for x, y in [
        ['0010', '4cffdf'],
        ['0011', '2de8f2'],
        ['0100', '759edb'],
        ['0110', 'ff5a71'],
        ['0000', 'ffffff'],
    ]},

    AxieClass.REPTILE: {x: y for x, y in [
        ['0010', 'fdbcff'],
        ['0011', 'ef93ff'],
        ['0100', 'f5e1ff'],
        ['0110', '43e27d'],
        ['0000', 'ffffff'],
    ]},

    AxieClass.MECH: {x: y for x, y in [
        ['0010', 'D9D9D9'],
        ['0011', 'D9D9D9'],
        ['0100', 'D9D9D9'],
        ['0110', 'D9D9D9'],
        ['0000', 'ffffff'],
    ]},

    AxieClass.DUSK: {x: y for x, y in [
        ['0010', 'D9D9D9'],
        ['0011', 'D9D9D9'],
        ['0100', 'D9D9D9'],
        ['0110', 'D9D9D9'],
        ['0000', 'ffffff'],
    ]},

    AxieClass.DAWN: {x: y for x, y in [
        ['0010', 'D9D9D9'],
        ['0011', 'D9D9D9'],
        ['0100', 'D9D9D9'],
        ['0110', 'D9D9D9'],
        ['0000', 'ffffff'],
    ]},
}


# Axie Region Mapping
class AxieRegion(Enum):
    Global = 'global'
    Japan = 'japan'


RegionMap = {
    # 256
    '00000': AxieRegion.Global,
    '00001': AxieRegion.Japan,
    # 512
    '000000000000000000': AxieRegion.Global
}


# Axie Tag Mapping
class AxieTag(Enum):
    Default = ''
    Origin = 'origin'
    Meo1 = 'meo1'
    Meo2 = 'meo2'
    Agamogenesis = 'agamogenesis'


TagMap = {
    # 256 Tags
    '00000': AxieTag.Default,
    '00001': AxieTag.Origin,
    '00010': AxieTag.Agamogenesis,
    '00011': AxieTag.Meo1,
    '00100': AxieTag.Meo2,
    # 512 Tags
    '0000000000': AxieTag.Default,
    '0000000001': AxieTag.Origin,
    '0000000010': AxieTag.Meo1,
    '0000000011': AxieTag.Meo2,
}


# Axie Body Skin Mapping
class AxieBodySkin(Enum):
    Normal = ''
    Frosty = 'frosty'


BodySkinMap = {
    '0000': AxieBodySkin.Normal,
    '0001': AxieBodySkin.Frosty,
}


# Axie Parts Mapping
class AxiePart(Enum):
    Eyes = 'eyes'
    Ears = 'ears'
    Mouth = 'mouth'
    Horn = 'horn'
    Back = 'back'
    Tail = 'tail'


class AxiePartSkin(Enum):
    Global = 'global'
    Mystic = 'mystic'
    Japan = 'japan'
    Xmas1 = 'xmas1'
    Xmas2 = 'xmas2'
    Bionic = 'bionic'


PartSkinMap = {
    # 256 Classes
    '00000': AxiePartSkin.Global,
    '00001': AxiePartSkin.Japan,
    '010101010101': AxiePartSkin.Xmas1,
    '01': AxiePartSkin.Bionic,
    '10': AxiePartSkin.Xmas2,
    '11': AxiePartSkin.Mystic,
    # 512 PartSkins
    '0000': AxiePartSkin.Global,
    '0001': AxiePartSkin.Mystic,
    '0011': AxiePartSkin.Japan,
    '0100': AxiePartSkin.Xmas1,
    '0101': AxiePartSkin.Xmas2,
    '0010': AxiePartSkin.Bionic,
}
