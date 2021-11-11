import numpy as np
import scipy

def add_one(number):
    return number + 1

def add_number_to_list(list_of_values, number):
    temp = np.array(list_of_values) + number
    return temp.tolist()