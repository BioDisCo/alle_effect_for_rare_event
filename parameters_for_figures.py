import numpy as np

"""
    This code contains the parameters used in the majority of the simulations.
    We list them:
    kappa = k
    rho = p
    P = P
    K = K
    n = n
"""

######################################################
# Parameters
K = 8e7
# K = 8e7-8e8 (or even lower values are possible) cells/mL
P = 1.5e8
# P = 1e8-1e9 cells/mL

n = 4
k = 35 # h-1
p = 14 # h-1
sigma = 0
# sigma_tr = 1.8 # h-1
sgvl = [0, 1.5, 3.04, 4, 5]
normalization_factor = 10
Hl = np.linspace(start=0, stop=P, num=10000)
######################################################

#####################################################
# Font and others
title_font = 15
axis_font = 12
#####################################################