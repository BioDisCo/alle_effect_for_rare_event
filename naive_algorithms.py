from mobspy import *
import matplotlib.pyplot as plt
import numpy as np
from parameters_for_figures import *

"""
    This code generates the naive algorithm calculations to compare with the alle-effect one
"""


def naive_broadcasting(duration, s):
    """
        Implementation of the naive broadcasting algorithm
    :param duration: simulation time duration
    :param s: value of sigma (rare event used)
    :return: final concentration of H
    """
    L, H = BaseSpecies(2)

    L >> H[s]
    L + H >> 2 * H[k]

    L(P)
    MySim = Simulation(L | H)
    MySim.plot_data = False
    MySim.save_data = False
    MySim.duration = duration
    MySim.level = 0
    MySim.run()

    return MySim.fres[H][-1]


def naive_sensor(duration, s):
    """
            Implementation of the naive sensor algorithm
        :param duration: simulation time duration
        :param s: value of sigma (rare event used)
        :return: final concentration of H
    """
    L, H = BaseSpecies(2)

    L >> H[s]
    H >> L[p]

    L(P)
    MySim = Simulation(L | H)
    MySim.plot_data = False
    MySim.save_data = False
    MySim.duration = duration
    MySim.level = 0
    MySim.run()

    return MySim.fres[H][-1]


def check_naive():
    """
        Passes a list of sigma values to both algorithms to construct the table
    """

    sgv_list = [0, 0.5, 1.8, 2, 3, 4]

    for s in sgv_list:
        print(s, naive_sensor(1000, s), naive_broadcasting(1000, s))
