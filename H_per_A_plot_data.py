from parameters_for_figures import *
import matplotlib.pyplot as plt
import pickle

with open('comparison.pkl', 'rb') as file:
    comp = pickle.load(file)

A_l, H_l, G_l, B_l, C_l = (comp['A_l'], comp['H_l'], comp['G_l'], comp['B_l'], comp['C_l'])

plt.xlabel(r'A (mL$^{-1}$)', fontsize=axis_font)
plt.ylabel(r'Reporters (mL$^{-1}$)', fontsize=axis_font)
plt.plot(A_l, C_l, label='Set-reset')
plt.plot(A_l, B_l, label='Broadcasting')
plt.plot(A_l, G_l, 'k-', label='Distributed amplification')
plt.plot(A_l, H_l, 'b-', label='Allee-based')
plt.legend()
plt.show()