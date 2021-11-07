# -*- coding: utf-8 -*-

# @Time     : 2021/11/3 1:47
# @Software : PyCharm
# @License  : GNU General Public License v3.0
# @Author   : xxx

"""The inner function:
   0       1      2     3     4      5       6       7      8      9      10     11      12
["add", "sub", "mul", "div", "ln", "exp", "pow2", "pow3", "rec", "max", "min", "sin", "cos"]
"""

import itertools

import numpy as np
import sympy

"""
Warnings!!!!
1. Do not use "-" and "/", x**n ,use sub and div,and pow2,pow3,
2. make sure each function has 2 input, for  one operation ,such as ln,exp, please set one placeholder: p, 
such as ln(x1,p),

"""
formulas = [
    "y=div((x1+x2),(x3+x4))",
    "y=(x1+x2)",
    "y=exp(div(x1,x2),p)",
    "y=sub(1,exp(div(x1,x2),p))",
    "y=x0+exp(div(x1,x2),p)",
    "y=div(x0,pow3(x1,p))",
    "y=ln(pow3(x1,p),p)",
    "y=sin(pow3(x1,p),p)",
    "y=sin(p,pow3(x1,p))",
]

xs = sympy.symbols("x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,xx,ss,p")
func_name_without_ = ["add", "sub", "mul", "div", "ln", "exp", "pow2", "pow3", "rec", "max", "min", "sin", "cos"]
xs = {i.name: i for i in xs}

fs = {i: sympy.Function(i) for i in func_name_without_}
xs.update(fs)

formulas2 = []
for i in formulas:
    i = i.replace("y=", "")
    assert "/" not in i, f"The {i} has '/' in sub expression, check it!"
    assert "-" not in i, f"The {i} has '/' in sub expression, check it!"
    i = eval(i, xs)
    formulas2.append(i)


def namess(expr):
    if isinstance(expr, sympy.Symbol):
        res = str(expr.name).lower()
    elif isinstance(expr, sympy.Integer):
        res = str(expr).lower()
    elif isinstance(expr, sympy.Expr):
        assert len(i.args) == 2, f"The {expr} has just one args in sub expression, check it!"
        res = {str(expr.__class__.__name__).lower(): [namess(ii) for ii in expr.args]}

    else:
        return str(expr).lower()
    return res


dict_name = []
for i in formulas2:
    dict_name.append(namess(i))


def poly_expand(n, now=0, power=5):
    if now > power:
        res = np.array([], dtype=np.int32)
    else:
        nn = (2 * n + np.array([1, 2], dtype=np.int32).reshape(2, 1)).ravel()
        res = np.append(nn, poly_expand(nn, now=now + 1, power=5))
    return res


def get_mark_tuple(dict_res):
    res = [[], [], [], [], [], [], [], [], []]

    def gm(dicti, lay=0):
        for k, v in dicti.items():
            res[lay].append(k)
            lay = lay + 1
            for i in v:
                if isinstance(i, dict):
                    gm(i, lay=lay)
                else:
                    res[lay].append(i)

    gm(dict_res)

    res = [i for i in itertools.chain(*res)]

    # print(res)

    index = np.arange(64).tolist()
    i = 0
    while i < len(res):
        if res[i] not in func_name_without_:
            index = set(index) - set(poly_expand(index[i]).tolist())
            index = list(index)
            index.sort()
        i += 1

    return index[:len(res)], res


def k_index(k):
    res = []
    for i in k:
        res.append((i - 1) // 2)
    return res


def k_label(k):
    res = []
    for i in k:
        try:
            res.append(func_name_without_.index(i))
        except ValueError:
            res.append(-1)
    return res


res = []
for i in dict_name:
    k, kk = get_mark_tuple(i)
    index = k_index(k)
    label = k_label(kk)
    res.append((tuple(index), tuple(label)))

with open("sci_formula.py", "w+")  as f:
    pre_str = [f"{str(i)},\n" for i in res]
    pre_str = "".join(pre_str)
    f.writelines(f"usr_preset = \\\n({str(pre_str)})")
