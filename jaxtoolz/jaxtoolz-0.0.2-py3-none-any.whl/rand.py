from random import randint
# returns a list of numbers of a certain length populated with random
#   integers between a and b including both
def randlist(length, a, b):
    l = []
    for i in range(length):
        l.append(randint(a, b))
    return l