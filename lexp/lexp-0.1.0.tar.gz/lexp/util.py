import re


def is_number(s):
    """
    判断字符串是否是数字
    :param s: 字符串
    :return: True/False
    """
    if s.count('.') < 2 and s.replace('.', '').isdigit():
        return True
    return False


def is_variable_name(s):
    """
    判断字符串是否是一个变量名
    :param s: 字符串
    :return: True/False
    """
    if s is None:
        return False
    m = re.match(r"^\d.*", s)
    if m is not None:
        return False
    wrong = [')', '(', '+', '-', '*', '/', '?', '!', ':', '>', '<', '=', '^']
    for w in wrong:
        if s.find(w) != -1:
            return False
    return True
    # m = re.match("^[_a-zA-Z\w]*$", s)
    # return False if m is None else True

