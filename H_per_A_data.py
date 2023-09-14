from mobspy import *
from parameters_for_figures import *
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pickle


# Our algorithm
# 300
A_l = [float(x) for x in np.linspace(0, 2e1, num=300)]
H_l = []
for i, e in enumerate(tqdm(A_l)):
    # print(i)
    L, H, E = BaseSpecies()

    L + E >> H + E[1]
    H >> L[p]

    L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

    L(P), E(e)
    S1 = Simulation(H | L | E)
    S1.duration = 10
    S1.level = 0
    S1.plot_data = False
    S1.run()
    H_l.append(S1.fres[H][-1])

# Their algorithm
G_l = []
for i, e in enumerate(tqdm(A_l)):
    # print(i)
    L, H, E, GFP = BaseSpecies()

    L + E >> H + E[1]
    H >> L[p]

    H >> H + GFP[lambda h: f'{k}*{h}*1/(1 + ({K}/{h})^{n})']
    L + H >> L + H + GFP[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']
    GFP >> Zero[40]
    # set to match at high E

    L(P), E(e)
    S1 = Simulation(H | L | E | GFP)
    S1.duration = 10
    S1.level = 0
    S1.plot_data = False
    S1.run()
    G_l.append(S1.fres[GFP][-1])

# Broadcasting
B_l = []
for i, e in enumerate(tqdm(A_l)):
    """
        Implementation of the naive broadcasting algorithm
    :param duration: simulation time duration
    :param s: value of sigma (rare event used)
    :return: final concentration of H
    """
    L, H, E = BaseSpecies()

    L + E >> H + E [1]
    L + H >> 2 * H[k]

    L(P), E(e)
    S = Simulation(L | H | E)
    S.plot_data = False
    S.duration = 10
    S.level = 0
    S.run()

    B_l.append(S.fres[H][-1])

# Classical sensor
C_l = []
for i, e in enumerate(tqdm(A_l)):
    """
        Implementation of the naive broadcasting algorithm
    :param duration: simulation time duration
    :param s: value of sigma (rare event used)
    :return: final concentration of H
    """
    L, H, E = BaseSpecies()

    L + E >> H + E [1]
    H >> L[p]

    L(P), E(e)
    S = Simulation(L | H | E)
    S.plot_data = False
    S.duration = 10
    S.level = 0
    S.run()

    C_l.append(S.fres[H][-1])


comp = {'A_l': A_l, 'H_l': H_l, 'G_l': G_l, 'B_l': B_l, 'C_l': C_l}

with open('comparison.pkl', 'wb') as file:
    pickle.dump(comp, file)