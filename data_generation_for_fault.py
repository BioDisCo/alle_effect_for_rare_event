from mobspy import *
import numpy as np
from parameters_for_figures import *
import matplotlib.pyplot as plt
import pickle

"""
    This code generates the noisy event rate that is used in the robustness simulation
    It performs a birth and death stochastic run on MobsPy with the parameters bellow
    The results are saved in a pickled file to be used in the robustness simulation
"""

pr = 0.5
dr = 2.2
dev = 1
acv = pr/dr
factor = dev/acv
factor = 1

E = BaseSpecies(1)
Zero >> E [pr]
E >> Zero [dr]

MySim = Simulation(E)
MySim.duration = 1000
MySim.step_size = 0.0001
MySim.save_data = False
MySim.plot_data = False
MySim.repetitions = 1
MySim.simulation_method = 'stochastic'
MySim.run()

"""
    In this step we clean up the data
    We only need to keep track of the rate changes and the time the change has occurred
    So we get rid of repeated points
"""
time_results = []
data_results = []
last_data_point = -1
for time, data in zip(MySim.fres['Time'], MySim.fres[E]):
    if last_data_point != data:
        print(data)
        last_data_point = data
        data_results.append(data*factor)
        time_results.append(time)

noise = {'Time':time_results, 'Data': data_results}

with open('noise_2.pkl', 'wb') as file:
    pickle.dump(noise, file)

