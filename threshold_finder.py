from mobspy import *
import numpy as np
from bdfunctions import *
import matplotlib.pyplot as plt


def search_thr(H):
    """
        This function finds the threshold using dichotomy search.
        It performs a search over sigma in [0, 100] and if dH/dt has three or one equilibrium points
    """

    e_start = 0
    e_finish = 100
    while abs(e_finish - e_start) > 1e-10:
        e = (e_start + e_finish)/2

        data = sum_lists(sum_lists(hill_plot(H), reset_plot(H)), sigma_plot(H, e))

        flag_1 = False
        flag_2 = False
        flag_3 = False
        flag_4 = False
        for d in data:

            if d >= 0:
                flag_1 = True
            if d < 0 and flag_1:
                flag_2 = True
            if d >= 0 and flag_2:
                flag_3 = True
            if d < 0 and flag_3:
                flag_4 = True

        assert flag_1
        assert flag_2

        # Case with three roots
        if flag_4:
            e_start = e
        else:
            e_finish = e

    return e


if __name__ == '__main__':
    print(search_thr(Hl))
