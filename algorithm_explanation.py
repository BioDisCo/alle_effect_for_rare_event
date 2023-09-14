import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt
from bdfunctions import *

sigmas = [0.1, 5]

"""
    This code generates figure comparing the set + hold rates with the reset rates.
    It generates the figure for two values of sigma 0.1 and 5, as portrait in the figure title
"""
for s in sigmas:
    H_bd =  np.linspace(start=0, stop=2e8, num=10000)
    set_l = sum_lists(hill_plot(Hl=H_bd, P=2e8), sigma_plot(Hl=H_bd, s=s, P=2e8))
    reset_l = []
    for r in reset_plot(Hl):
        reset_l.append(-r)

    plt.xlabel('H (mL$^{-1}$)', fontsize=axis_font)
    plt.ylabel('Rates (mL$^{-1}$ h$^{-1}$)', fontsize=axis_font)
    plt.plot(Hl, set_l, label='Set + Hold')
    plt.plot(Hl, reset_l, label='Reset')
    plt.legend()
    plt.show()


