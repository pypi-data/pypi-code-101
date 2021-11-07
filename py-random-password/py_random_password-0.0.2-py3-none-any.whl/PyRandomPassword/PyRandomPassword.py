#!/usr/bin/env python
# Author : Sujit Mandal
import random
import array


#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""


def RandomGeneratePassword(password_length):
    DIGITS = ['2', '3', '4', '5', '6', '7', '8', '9']

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 
                        't', 'u', 'v', 'w', 'x', 'y', 'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    SYMBOLS = ['@', '#', '$', '%','?', '*',]


    caracters_list = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS


    random_digit = random.choice(DIGITS)
    random_upper = random.choice(UPCASE_CHARACTERS)
    random_lower = random.choice(LOCASE_CHARACTERS)
    random_symbol = random.choice(SYMBOLS)


    temp_password = random_digit + random_upper + random_lower + random_symbol

    for x in range(password_length - 4):
        temp_password = temp_password + random.choice(caracters_list)
        temp_password_list = array.array('u', temp_password)
        random.shuffle(temp_password_list)


    password = ""
    for i in temp_password_list:
        password = password + i

    return(password)



if __name__ == '__main__':
    password_length = 8
    password = RandomGeneratePassword(password_length)
    print('Password : {}'.format(password))