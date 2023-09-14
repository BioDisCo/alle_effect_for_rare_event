from mobspy import *
import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt
import pickle


duration = 100
"""
    This code generates the robustness figure and simulation
    It does so by performing a hybrid simulation by adding the noisy event rate as events in MobsPy
    At the time of writting this, events are only available in the MobsPy github
"""

# Perturbation Resistance
with open('noise_2.pkl', 'rb') as file:
    noise = pickle.load(file)

L, H, A = BaseSpecies(3)

L + A >> H + A[1]
H >> L[p]
L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

L(P)
S1 = Simulation(H | L | A)

for time, data in zip(noise['Time'], noise['Data']):
    with S1.event_time(time):
        A(data)

S1.save_data = False
S1.plot_data = False
S1.step_size = 0.01
S1.duration = duration
S1.run()
R = S1.fres

# Steady state alpha_f value
L, H, A = BaseSpecies(3)

L >> H [0]
H >> L[p]
L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

H(P)
S2 = Simulation(H | L)
S2.save_data = False
S2.plot_data = False
S2.duration = duration
S2.run()
R2 = S2.fres

plt.plot(R['Time'], [x for x in R[H]], 'b-', label=f'H')
plt.plot(R2['Time'], [R2[H][-1] for _ in R2['Time']], label=r'$\alpha_{f}$', color='#808080', linestyle='dashed')

plt.ylabel('H (mL$^{-1}$)', fontsize=axis_font)
plt.xlabel('Time (h)', fontsize=axis_font)
plt.legend(loc='center left')

ax2 = plt.twinx()
ax2.plot(R['Time'], [5*x/R['Time'][-1] for x in R['Time']], color='w')
ax2.plot(R['Time'], [x for x in R[A]], color='#C9ADA7', linestyle='dashed', label=f'Noise')
ax2.plot(R['Time'], [3 for x in R[A]], color='#22223B', linestyle='dashed', label=r'$\sigma_{c}$')
ax2.set_ylabel(r'Noise intensity (h$^{-1}$)', fontsize=axis_font)
ax2.legend(loc='center right')

plt.show()


