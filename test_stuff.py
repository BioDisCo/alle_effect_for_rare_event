import numpy as np
from bdfunctions import *
import matplotlib.pyplot as plt

xl = np.linspace(start=0, stop=P, num=1000)

yl = sum_lists(hill_plot(xl, k, n), reset_plot(xl, p))
plt.plot(xl, yl)

zl = zero_reference(xl)
plt.plot(xl, zl, color='#808080', label='Zero', linestyle='dashed')
plt.legend()
plt.title(r'$\frac{dH}{dt}$ ' + ' P = ' + r'$2*10^8$ Heatmap', fontsize=title_font)
plt.xlabel('H Concentration ' + r'$\frac{cells}{mL}$', fontsize=axis_font)
plt.ylabel(r'$\frac{dH}{dt}$ ' + ' ' + r'$\frac{cells}{mL \cdot h}$', fontsize=axis_font)
plt.show()



