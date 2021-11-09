import matplotlib.pyplot as plt

import numpy as np


def plotPercentiles(x, data, ax, lb=0, ub=100, n=21, cmap=plt.cm.Blues):
    
    percentiles = np.linspace(lb, ub, n)
    limits = [np.percentile(data, per, 0) for per in percentiles]

    c= cmap(0.5)
    ax.plot(x, data.mean(0), '-', c=c)
    ax.plot(x, np.percentile(data, 0, 0), '--', c=c);
    ax.plot(x, np.percentile(data, 25, 0), '--', c=c);
    ax.plot(x, np.percentile(data, 50, 0), '--', c=c);
    ax.plot(x, np.percentile(data, 75, 0), '--', c=c);
    ax.plot(x, np.percentile(data, 100, 0), '--', c=c);
    
    half = int((n-1)/2)
    for i in range(half):
        ax.fill_between(x, limits[i], limits[-(i+1)], color=cmap(i/half), alpha=0.5)