from mobspy import *
import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt

"""
    This code generates the convergence table and also considers cell reproduction and death calculations
"""

def find_convergence_times():

    def run_sim(s, duration):
        Cell = BaseSpecies(1)
        L, H = New(Cell, 2)

        # Comment both these lines to remove reproduction and death reactions
        Cell >> 2*Cell [0.5]
        Cell >> Zero [0.5]
        ####################################################################

        L >> H[s]
        H >> L[p]
        L + H >> 2 * H[lambda l, h: f'{k}*{l}*1/(1 + ({K}/{h})^{n})']

        L(P)
        MySim = Simulation(L | H)
        MySim.plot_data = False
        MySim.save_data = False
        MySim.duration = duration
        MySim.level = 0
        MySim.run()

        return MySim, MySim.results['L'][-1]

    sgv_list = [0, 0.5, 1.8, 2,  3, 4]

    for s in sgv_list:
        duration_b = 1e-10
        duration_f = 10

        Sim, std_state_value = run_sim(s, 1000)

        while abs(duration_f - duration_b) > 1e-10:
            duration = (duration_f + duration_b)/2

            Sim, L_value = run_sim(s, duration)
            percentage = abs(L_value - std_state_value)/std_state_value

            if percentage < 0.05:
                duration_f = duration
            else:
                duration_b = duration
        Sim.plot_deterministic()

        print(s, duration, P-std_state_value)


find_convergence_times()

