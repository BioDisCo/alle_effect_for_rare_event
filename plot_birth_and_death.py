from mobspy import *
import numpy as np
from parameters_for_figures import *
from bdfunctions import *
import matplotlib.pyplot as plt

"""
    This code generates the dH/dt figure for the R1, R2 and R3 regions detailed on the paper
    The parameters for rho and kappa are locates in the list params 
"""

params = [(10, 175), (70, 100), (70, 7)]
xl = np.linspace(start=0, stop=P, num=1000)

for i, (p, k) in enumerate(params):
    i = i + 1
    yl = sum_lists(hill_plot(xl, k, n), reset_plot(xl, p))
    plt.plot(xl, yl, label=f'R{i}')

zl = zero_reference(xl)
plt.plot(xl, zl, color='#808080', label='Zero', linestyle='dashed')
plt.legend()
# plt.title(r'$\frac{dH}{dt}$ ' + ' P = ' + r'$2*10^8$ Heatmap', fontsize=title_font)
plt.xlabel('H ' + r'(mL$^{-1})$', fontsize=axis_font)
plt.ylabel(r'$\frac{dH}{dt}$ ' + ' ' + r'(mL$^{-1}$ h$^{-1}$)', fontsize=axis_font)
plt.show()

