"""
Freedom test task solution.

free.py

Peter Mawhorter 2021-7-23
"""


def whatever(a, b):
    """
    We don't care what you return from this function, as long as you
    return different values when the arguments are both True, both
    False, or when one is True and the other is False. You must return
    the same value when one is True and the other is False regardless of
    which argument is True and which is False.
    """
    if a and b:
        return "Both"
    elif a or b:
        return "One"
    else:
        return "Neither"


# Expectations

import optimism as opt

opt.testCase(whatever(True, True))
opt.expectResult("Both")
opt.testCase(whatever(True, False))
opt.expectResult("One")
opt.testCase(whatever(False, True))
opt.expectResult("One")
opt.testCase(whatever(False, False))
opt.expectResult("Neither")
