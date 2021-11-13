from azhida_tools import mysql
from azhida_tools import tool


def fn_print(str):
    res1 = tool.test(str)
    print(res1)
    res2 = mysql.test(str)
    print(res2)


fn_print('abcd')
