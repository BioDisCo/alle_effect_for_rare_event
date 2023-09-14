import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt
import matplotlib
from bdfunctions import *
from tqdm import tqdm
import pickle

# For now I generate them one by one for time reasons
Pl = [0.25e8, 0.5e8, 1e8, 2e8, 6e8, 1e9]
# P = 0.3e8
"""
    This code generates the data for the heatmaps
    It does so by performing the calculations and saving in a pickle file
    The population concentrations can be located at the Pl list above
    And for the parameters kappa and pho, we vary up to five times above and divided 
"""


def rough_threshold_estimation(P, k, n, p):
    # 10000
    xl = np.linspace(start=0, stop=P, num=1000)
    yl = sum_lists(hill_plot(xl, k, n), reset_plot(xl, p))

    ini_neg_flag = True
    greatest_sigma = 0
    for x, y in zip(reversed(xl),reversed(yl)):

        if ini_neg_flag:
            if y > 0:
                ini_neg_flag = False
            else:
                continue

        if y < 0:
            sv = y/(x - P)
            if sv > greatest_sigma:
                greatest_sigma = sv

    return greatest_sigma


kl = np.linspace(start=k/5, stop=5*k, num=1000)
pl = np.linspace(start=p/5, stop=5*p, num=1000)

for P in Pl:
    matrix = []
    for k in tqdm(kl):
        line = []
        for p in pl:
            line.append(rough_threshold_estimation(P, k, n, p))
        matrix.append(line)

    for i in range(8):
        P = P / 10

    with open(f'{P}_10_8.pkl', 'wb') as file:
        pickle.dump(matrix, file)



