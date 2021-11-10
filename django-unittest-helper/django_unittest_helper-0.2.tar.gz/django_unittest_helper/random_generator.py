from random import randint


def generate_random_phone_no(prefix: str, total_digit: int):
    """
    :param prefix: <class 'str'>
    :param total_digit: <class 'int'>
    :return: <class 'str'>
    """
    digit_no = total_digit - len(prefix)
    res = str(prefix) + str(randint(int('1' * digit_no), int('9' * digit_no)))
    return res

