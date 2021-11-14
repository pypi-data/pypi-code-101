import platform

version = '0.1.1'

IS = platform.system()

if IS == 'Windows':
    from ._windows import sequence as _sequence
elif IS == 'Linux':
    from ._linux import sequence as _sequence
elif IS == 'Darwin':
    from ._darwin import sequence as _sequence
else:
    raise OSError("Unsupported platform '{}'".format(platform.system()))


kdict = {
    "left ctrl":        (29,    17,     59,     29),
    "right ctrl":       (157,   17,     62,     97),

    "left shift":       (42,    16,     56,     42),
    "right shift":      (54,    16,     60,     54),

    "left alt":         (56,    18,     58,     56),
    "left option":      (56,    18,     58,     56),

    "right alt":        (184,   18,     61,     100),
    "right option":     (184,   18,     61,     100),

    "left win":         (219,   91,     55,     125),
    "left cmd":         (219,   91,     55,     125),

    "right win":        (220,   92,     54,     126),
    "right cmd":        (220,   92,     54,     126),

    "esc":              (1,     27,     53,     1),
    "1":                (2,     49,     18,     2),
    "2":                (3,     50,     19,     3),
    "3":                (4,     51,     20,     4),
    "4":                (5,     52,     21,     5),
    "5":                (6,     53,     23,     6),
    "6":                (7,     54,     22,     7),
    "7":                (8,     55,     26,     8),
    "8":                (9,     56,     28,     9),
    "9":                (10,    57,     25,     10),
    "0":                (11,    48,     29,     11),
    "-":                (12,    189,    27,     12),
    "=":                (13,    187,    24,     13),
    "backspace":        (14,    8,      51,     14),
    "tab":              (15,    9,      48,     15),
    "q":                (16,    81,     12,     16),
    "w":                (17,    87,     13,     17),
    "e":                (18,    69,     14,     18),
    "r":                (19,    82,     15,     19),
    "t":                (20,    84,     17,     20),
    "y":                (21,    89,     16,     21),
    "u":                (22,    85,     32,     22),
    "i":                (23,    73,     34,     23),
    "o":                (24,    79,     31,     24),
    "p":                (25,    80,     35,     25),
    "[":                (26,    219,    33,     26),
    "]":                (27,    221,    30,     27),
    "enter":            (28,    13,     36,     28),
    "a":                (30,    65,     0,      30),
    "s":                (31,    83,     1,      31),
    "d":                (32,    68,     2,      32),
    "f":                (33,    70,     3,      33),
    "g":                (34,    71,     5,      34),
    "h":                (35,    72,     4,      35),
    "j":                (36,    74,     38,     36),
    "k":                (37,    75,     40,     37),
    "l":                (38,    76,     37,     38),
    ";":                (39,    186,    41,     39),
    "'":                (40,    222,    39,     40),
    "`":                (41,    192,    50,     41),
    "\\":               (43,    220,    42,     43),
    "z":                (44,    90,     6,      44),
    "x":                (45,    88,     7,      45),
    "c":                (46,    67,     8,      46),
    "v":                (47,    86,     9,      47),
    "b":                (48,    66,     11,     48),
    "n":                (49,    78,     45,     49),
    "m":                (50,    77,     46,     50),
    "comma":            (51,    188,    43,     51),
    ".":                (52,    190,    47,     52),
    "/":                (53,    191,    44,     53),
    "space":            (57,    32,     49,     57),
    "caps lock":        (58,    20,     57,     58),
    "f1":               (59,    112,    122,    59),
    "f2":               (60,    113,    120,    60),
    "f3":               (61,    114,    99,     61),
    "f4":               (62,    115,    118,    62),
    "f5":               (63,    116,    96,     63),
    "f6":               (64,    117,    97,     64),
    "f7":               (65,    118,    98,     65),
    "f8":               (66,    119,    100,    66),
    "f9":               (67,    120,    101,    67),
    "f10":              (68,    121,    109,    68),
    "num 7":            (71,    103,    89,     71),
    "num 8":            (72,    104,    91,     72),
    "num 9":            (73,    105,    92,     73),
    "num 4":            (75,    100,    86,     75),
    "num 5":            (76,    101,    87,     76),
    "num 6":            (77,    102,    88,     77),
    "num 1":            (79,    97,     83,     79),
    "num 2":            (80,    98,     84,     80),
    "num 3":            (81,    99,     85,     81),
    "num 0":            (82,    96,     82,     82),
    "f11":              (87,    122,    103,    87),
    "f12":              (88,    123,    111,    88),

    "num lock":         (197,   144,    0,      69),                # todo Darwin
    "clear":            (0,     0,      71,     0),                 # todo Windows, Linux
    "num equal":        (0,     0,      81,     0),   # num =       # todo Windows, Linux

    "num divide":       (181,   111,    75,     98),  # num /
    "num multiply":     (55,    106,    67,     55),  # num *
    "num subtract":     (74,    109,    78,     74),  # num -
    "num add":          (78,    107,    69,     78),  # num +
    "num enter":        (156,   13,     76,     96),
    "num decimal":      (83,    110,    65,     83),  # num .
    "home":             (199,   36,     115,    102),
    "up arrow":         (200,   38,     126,    103),
    "page up":          (201,   33,     116,    104),
    "left arrow":       (203,   37,     123,    105),
    "right arrow":      (205,   39,     124,    106),
    "end":              (207,   35,     119,    107),
    "down arrow":       (208,   40,     125,    108),
    "page down":        (209,   34,     121,    109),
    "delete":           (211,   46,     117,    111),

    "insert":           (210,   45,     0,      110),               # todo Darwin
    "pause":            (69,    19,     0,      119),               # todo Darwin
    "scroll lock":      (70,    145,    0,      70),                # todo Darwin
}


def tap(sequence, delay=0.05):
    sequence = list(map(str.strip, sequence.split(',')))
    for combination in sequence:
        combination = list(map(str.strip, combination.split('+')))
        codes = []
        for shortcut in combination:
            code = kdict.get(shortcut)
            if code:
                codes.append(code)
            else:
                print("Unknown key: " + shortcut)
        _sequence(codes, delay)
    return
