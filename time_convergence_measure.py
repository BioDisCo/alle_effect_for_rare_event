from mobspy import *
import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt

"""
    This code generate the plots of H(t) for different values of sigma
    sgvl can be found in the parameter code
"""

for s in reversed(sgvl):

    if s == 0:
        continue

    L, H = BaseSpecies(2)

    L >> H[s]
    H >> L[p]
    L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

    L(P)
    S1 = Simulation(H | L)
    S1.save_data = False
    S1.plot_data = False
    S1.duration = 10
    S1.step_size = 0.01
    S1.level = -1
    S1.run()
    R = S1.fres

    for t, value in zip(R['Time'], R['H']):

        if abs(R['H'][-1] - value)/R['H'][-1] < 0.05:
            print(s, t, R['H'][-1])
            break

