# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['handyderivatives']

package_data = \
{'': ['*']}

install_requires = \
['sympy>=1.7.1,<2.0.0']

entry_points = \
{'console_scripts': ['handyderivatives = handyderivatives:runner']}

setup_kwargs = {
    'name': 'handyderivatives',
    'version': '2.3.1',
    'description': 'Calc. on the command line - with LaTeX output.',
    'long_description': "# handyderivatives\n\n[PyPi link](https://pypi.org/project/handyderivatives/)\n\nA command line program to do some differential calculus.\nThis is essentially a wrapper for some of [SymPy's](https://github.com/sympy/sympy) calculus tools.\n[Here is SymPy's calculus documentation.](https://docs.sympy.org/latest/tutorial/calculus.html)\n\n\n*Right now it has the functionality listed below.*\n\n- Differentiate elementary functions.\n- Get the gradient of a scalar field.\n\n\n## Installation\n```\npip3 install handyderivatives\n```\n\n## Running it\nTo get the derivatives for an arbitrary number of functions of a single variable.\n\n```\nhandyderivatives -d 'f(x) = x ^ 2' 'g(x) = sin(x) + 2 * x'\n```\n\nTo get the gradient for an arbitrary number of scalar functions.\n\n```\nhandyderivatives -g 'f(x,y,z) = ln(x / (2 * y)) - z^2 * (x - 2 * y) - 3*z'\n```\nOr run that with one command.\n\n```\nhandyderivatives -d 'f(x) = x ^ 2' 'g(x) = sin(x) + 2 * x' -g 'f(x,y,z) = ln(x / (2 * y)) - z^2 * (x - 2 * y) - 3*z'\n```\n\nTo differentiate a list of functions in a file and output that to a LaTeX document.\n\n```\nhandyderivatives --latex -f functions.txt\nhandyderivatives -l -f functions.txt\n```\n\nThe `-l` flag can also be used in the earlier examples.\n\n### Help\n```\nusage: handyderivatives [-h] [--input-file FILE] [--latex] [--diff [DIFFERENTIAL [DIFFERENTIAL ...]]] [--gradient [GRADIENT [GRADIENT ...]]]\n\nCommand line differential calculus tool using SymPy.\nTry running:\nhandyderivatives -l -g 'f(x,y) = sin(x) * cos(y)'\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --input-file FILE, -f FILE\n                        Input file\n  --latex, -l           Compile a LaTeX document as output\n  --diff [DIFFERENTIAL [DIFFERENTIAL ...]], -d [DIFFERENTIAL [DIFFERENTIAL ...]]\n                        Works for equations written in the form  'f(x) = x ^2'\n  --gradient [GRADIENT [GRADIENT ...]], -g [GRADIENT [GRADIENT ...]]\n                        Works for scalar functions written in form  'f(x,y,z) = x ^2 * sin(y) * cos(z)'\n```\n\n## How the input file should be formatted\nEdit a file that has functions listed one per line.\nThe left hand side should be what your function will be differentiated with respect to, i.e *f(x)* .\nThe right hand side will be the expression.\n\n```\n# This is how the file for the argument -f should be formatted.\n\nc(x) = r * (cos(x) + sqrt(-1) * sin(x))\na(t) = 1/2 * g * t ** 2\nf(x) = sin(x**2) * x^2\nh(w) = E ^ (w^4 - (3 * w)^2 + 9) # Capital E is interpreted by SymPy as the base of the natural log.\ng(x) = exp(3 * pi)               # So is exp(x), but written as a function taking an argument.\np(j) = csc(j^2)\n```\n\nIf you don't format it like that you will likely run into errors.\nYou  can add comments.\n\n<!--\n## TODO\n- Importing things from SymPy takes up a significant amount of time when the program first loads.\nRight now it's the main bottleneck, maybe there's some way to do this faster.\n- Add divergence.\n\n## Sample PDF\n\n![PDF-Example](https://raw.githubusercontent.com/Fitzy1293/handyderivatives/main/images/output.png)\n-->\n",
    'author': 'fitzy1293',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fitzy1293/handyderivatives',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
