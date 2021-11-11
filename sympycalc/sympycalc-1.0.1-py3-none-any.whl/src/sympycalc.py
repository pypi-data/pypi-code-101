from math import *
import argparse
from sympy import *
from sympy.plotting import *
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('expr', nargs='+', help='Expression')
    args = parser.parse_args()
    expr = args.expr
    index=0
    if expr[0]=='s':
        x, y, z, t = symbols('x y z t')
        f, g, h = symbols('f g h', cls=Function)
        index = 1
    for i in expr[index:]:
        try:
            print(eval(i))
        except:
            exec(i)
