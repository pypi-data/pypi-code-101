import numpy as np
import matplotlib.pyplot as plt

def interpolate_function(x, y):
    length = len(x)
    m = [[it ** j for j in range(length)] for it in x]
    constants = np.linalg.solve(m, y)
    return lambda val: np.sum(constants * [val ** i for i in range(length)])

def plot(x, y):
    n = min(len(x), len(y))
    xy = [[x[i], y[i]] for i in range(n)]
    xy.sort()
    x = [xy[i][0] for i in range(n)]
    y = [xy[i][1] for i in range(n)]
    newx =  np.linspace(min(x), max(x), len(x) * 10)
    f = interpolate_function(x, y)

    plt.plot(x, y, 'o', newx, [f(it) for it in newx], '--')
    
def printQ():
    print("QQQQQQQQQQ")