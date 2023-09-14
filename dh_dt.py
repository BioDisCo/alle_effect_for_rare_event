import numpy as np
from parameters_for_figures import *
from bdfunctions import *
import matplotlib.pyplot as plt

"""
    This code generates the plots of dH/dt for different values of sigma
"""


def paper_figure_equilibrium_points(Hl):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for sig in sgvl:
        data = sum_lists(sum_lists(hill_plot(Hl), reset_plot(Hl)), sigma_plot(Hl, sig))
        ax.plot(Hl, data, label=r'$\sigma=$' + str(sig) + r' h$^{-1}$')

    ax.plot(Hl, zero_reference(Hl), label='Zero Axis')
    plt.xlabel(r'H (mL$^{-1}$)', fontsize=axis_font)
    plt.ylabel(r'$\frac{dH}{dt}$ (mL$^{-1}$ h$^{-1}$)', fontsize=axis_font)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc='lower left')

    plt.show()


if __name__ == '__main__':
    paper_figure_equilibrium_points(Hl)
