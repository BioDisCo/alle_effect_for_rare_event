from mobspy import *
import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt


"""
    This code generates the figure where H(t) is exposed to several different amplitudes for event rate.
    The amplitudes vary, but the time changes
    The amplitude rates can be found in the amplitude list
    The epsilon is used to make the plot more visible
"""

amplitudes = [2, 4, 6]
Hc = ['#004C99','#4C0099','#4C9900']
Ac = ['#0080FF','#7F00FF','#66CC00']
epsilon = [0, 0.002, 0.004]

event_results = []
for i, (a, hc, ec, e) in enumerate(zip(amplitudes, Hc, Ac, epsilon)):
    L, H, A = BaseSpecies(3)

    L + A >> H + A[1]
    H >> L[p]
    L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

    L(P)
    S1 = Simulation(H | L | A)

    with S1.event_time(0.1):
        A(a)

    with S1.event_time(0.3):
        A(0)

    S1.save_data = False
    S1.plot_data = False
    S1.duration = 0.6
    S1.run()
    R = S1.fres
    plt.plot(R['Time'], [x for x in R[H]], label=rf'$H_{i}$', color=hc)
    event_results.append(([e + x for x in R['A']], i, ec))

plt.ylabel('H (mL$^{-1}$)', fontsize=axis_font)
plt.xlabel('Time (h)', fontsize=axis_font)

L, H, E = BaseSpecies(3)

L >> H [0]
H >> L [p]
L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

H(P)
S2 = Simulation(H | L)
S2.save_data = False
S2.plot_data = False
S2.duration = 0.6
S2.run()
R = S2.fres

plt.plot(R['Time'], [R[H][-1] for _ in R['Time']], label=r'$\alpha_f P$', color='#808080', linestyle='dashed')
plt.tick_params(axis='y')
plt.legend()

ax2 = plt.twinx()

for r in event_results:
    ax2.plot(R['Time'], r[0], label=rf'$A_{r[1]}$', color=r[2])

ax2.set_ylabel('A (mL$^{-1}$)', fontsize=axis_font)

ax2.tick_params(axis='y')

plt.legend()
plt.show()
