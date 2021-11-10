import matplotlib.pyplot as plt

def print_histprint_hist(height, x, rwidth = 0.9):
    wdth = x[1] - x[0] if len(x) > 1 else 1
    x = [x[i] + wdth / 2  for i in range(len(x) - 1)]
    plt.bar(x = x, height = height, width = wdth * rwidth)