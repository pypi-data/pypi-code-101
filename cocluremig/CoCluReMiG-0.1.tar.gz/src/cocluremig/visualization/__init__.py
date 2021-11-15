"""
Graph visualization modules
"""
from typing import List

"""DOT_COLORS: List[str] = [c.strip()
                         for c in open(
        os.path.dirname(
            os.path.abspath(__file__)) +
        os.path.sep + "colors_short.csv")]"""
DOT_COLORS: List[str] = ['aliceblue', 'antiquewhite', 'aqua',
                         'aquamarine', 'azure', 'beige',
                         'bisque', 'black', 'blanchedalmond',
                         'blue', 'blueviolet', 'brown',
                         'burlywood', 'cadetblue', 'chartreuse',
                         'chocolate', 'coral', 'cornflowerblue',
                         'cornsilk', 'crimson', 'cyan', 'darkblue',
                         'darkcyan', 'darkgoldenrod', 'darkgray',
                         'darkgreen', 'darkgrey', 'darkkhaki',
                         'darkmagenta', 'darkolivegreen', 'darkorange',
                         'darkorchid', 'darkred', 'darksalmon',
                         'darkseagreen', 'darkslateblue', 'darkslategray',
                         'darkslategrey', 'darkturquoise', 'darkviolet',
                         'deeppink', 'deepskyblue', 'dimgray',
                         'dimgrey', 'dodgerblue', 'firebrick',
                         'floralwhite', 'forestgreen', 'fuchsia',
                         'gainsboro', 'ghostwhite', 'gold',
                         'goldenrod', 'green', 'greenyellow',
                         'grey', 'honeydew', 'hotpink',
                         'indianred', 'indigo', 'invis',
                         'ivory', 'khaki', 'lavender',
                         'lavenderblush', 'lawngreen',
                         'lemonchiffon', 'lightblue', 'lightcoral',
                         'lightcyan', 'lightgoldenrod', 'lightgoldenrodyellow',
                         'lightgray', 'lightgreen', 'lightgrey',
                         'lightpink', 'lightsalmon', 'lightseagreen',
                         'lightskyblue', 'lightslateblue', 'lightslategray',
                         'lightslategrey', 'lightsteelblue', 'lightyellow',
                         'lime', 'limegreen', 'linen',
                         'magenta', 'maroon', 'mediumaquamarine',
                         'mediumblue', 'mediumorchid',
                         'mediumpurple', 'mediumseagreen', 'mediumslateblue',
                         'mediumspringgreen', 'mediumturquoise',
                         'mediumvioletred', 'midnightblue', 'mintcream',
                         'mistyrose', 'moccasin', 'navajowhite', 'navy',
                         'navyblue', 'none', 'oldlace', 'olive',
                         'olivedrab', 'orange', 'orangered',
                         'orchid', 'palegoldenrod', 'palegreen',
                         'paleturquoise', 'palevioletred', 'papayawhip',
                         'peachpuff', 'peru', 'pink', 'plum',
                         'powderblue', 'purple', 'rebeccapurple',
                         'red', 'rosybrown', 'royalblue', 'saddlebrown',
                         'salmon', 'sandybrown', 'seagreen', 'seashell',
                         'sienna', 'silver', 'skyblue',
                         'slateblue', 'slategray',
                         'slategrey', 'snow', 'springgreen',
                         'steelblue', 'tan', 'teal',
                         'thistle', 'tomato', 'transparent',
                         'turquoise', 'violet', 'violetred',
                         'webgray', 'webgreen', 'webgrey',
                         'webmaroon', 'webpurple', 'wheat',
                         'white', 'whitesmoke',
                         'yellow', 'yellowgreen']
"""
All available dot base colors
"""
