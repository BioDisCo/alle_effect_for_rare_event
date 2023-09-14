from mobspy import *
import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt


# Exposure Times
"""
    This code generates the figure where H(t) is exposed to several different times for the same event rate amplitude.
    The times can be found in the time list
    The epsilon is used to make the plot more visible
"""

times = [0.15, 0.3, 0.45]
Hc = ['#004C99','#4C0099','#4C9900']
Ac = ['#0080FF','#7F00FF','#66CC00']
epsilon = [0, 0.002, 0.004]

event_results = []
for i, (t, hc, ec, e) in enumerate(zip(times, Hc, Ac, epsilon)):
    L, H, A = BaseSpecies(3)

    L + A >> H + A[1]
    H >> L[p]
    L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

    L(P), A(sgvl[3])
    S1 = Simulation(H | L | A)

    with S1.event_time(t):
        A(0)

    S1.save_data = False
    S1.plot_data = False
    S1.duration = 1.2
    S1.run()
    R = S1.fres
    factor = 1/normalization_factor

    plt.plot(R['Time'], [x/P for x in R[H]], label=rf'H t={t} h', color=hc)
    event_results.append(([e + x * factor for x in R['A']], i, ec))


L, H, A = BaseSpecies(3)

L >> H [0]
H >> L[p]
L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

H(P)
S2 = Simulation(H | L)
S2.save_data = False
S2.plot_data = False
S2.duration = 0.8
S2.run()
R = S2.fres

plt.plot(R['Time'], [R[H][-1]/P for _ in R['Time']], label=r'$\alpha_f P$', color='#808080', linestyle='dashed')
plt.ylabel(r'H (mL$^{-1}$)', fontsize=axis_font)
plt.xlabel('Time (h)', fontsize=axis_font)
plt.legend()

ax2 = plt.twinx()

for r in event_results:
    ax2.plot(R['Time'], r[0], label=rf'A$_{r[1]}$', color=r[2])

ax2.set_ylabel(r'A (mL$^{-1}$)', fontsize=axis_font)

ax2.tick_params(axis='y')

plt.legend()
plt.show()
