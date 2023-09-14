import pickle
import matplotlib.pyplot as plt
import numpy as np
from parameters_for_figures import *

"""
    This code generates the heatmap images from the pickle files with the calculations
"""

names = ['0.25_10_8.pkl', '0.5_10_8.pkl', '2.0_10_8.pkl', '6.0_10_8.pkl', '10.0_10_8.pkl']

data_list = []
for name in names:
    with open(name, 'rb') as file:
        data_list.append(pickle.load(file))

# change this if necessary
kl = np.linspace(start=k/5, stop=5*k, num=1000)
pl = np.linspace(start=p/5, stop=5*p, num=1000)

for name, data in zip(names, data_list):

    picture_name = name[:-4]
    picture_name = picture_name + '.png'

    fig, ax = plt.subplots()
    im = ax.imshow(data)
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel(r'$\sigma$' + ' Threshold (h$^{-1})$', rotation=-90, va="bottom")
    tick_p = [pl[0], pl[int(len(pl) * 1 / 4 - 1)], pl[int(len(pl) * 1 / 2 - 1)], pl[int(len(pl) * 3 / 4 - 1)],
              pl[int(len(pl) - 1)]]
    tick_k = [kl[0], kl[int(len(pl) * 1 / 4 - 1)], kl[int(len(pl) * 1 / 2 - 1)], kl[int(len(pl) * 3 / 4 - 1)],
              kl[int(len(pl) - 1)]]

    v = name.split('_')[0]

    ax.set_xticks(list(np.arange(0, len(pl), len(pl) / 4, dtype=int)) + [len(pl) - 1])
    ax.set_xticklabels([str(round(p, 1)) for p in tick_p])
    ax.set_yticks(list(np.arange(0, len(kl), len(kl) / 4, dtype=int)) + [len(kl) - 1])
    ax.set_yticklabels([str(round(k, 1)) for k in tick_k])

    plt.xlabel(r'$\rho$ (h$^{-1})$', fontsize=axis_font)
    plt.ylabel(r'$\kappa$ (h$^{-1})$', fontsize=axis_font)
    plt.savefig(picture_name)

