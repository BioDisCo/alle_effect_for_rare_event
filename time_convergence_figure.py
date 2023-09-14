from mobspy import *
import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt

"""
    This code generate the plots of H(t) for different values of sigma
    sgvl can be found in the parameter code
"""

L, H, E = BaseSpecies(3)

L >> H [0]
H >> L[p]
L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

H(P)
S2 = Simulation(H | L)
S2.save_data = False
S2.plot_data = False
S2.duration = 0.6
S2.run()
R = S2.fres

plt.plot(R['Time'], [R[H][-1] for _ in R['Time']], label=r'$\alpha_f P$', color='#808080', linestyle='dashed')
plt.xlabel('Time (h)', fontsize=axis_font)
plt.ylabel(r'H (mL$^{-1})$', fontsize=axis_font)

for s in reversed(sgvl):

    L, H = BaseSpecies(2)

    L >> H[s]
    H >> L[p]
    L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

    L(P)
    S1 = Simulation(H | L)
    S1.save_data = False
    S1.plot_data = False
    S1.duration = 0.6
    S1.run()
    R = S1.fres

    plt.plot(R['Time'], R['H'], label= rf'$\sigma$={s}' + r' h$^{-1}$')


plt.legend()
plt.show()

