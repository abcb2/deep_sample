# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def func(x0, x1):
    return x0 ** 2 + x1 ** 2


x0 = np.arange(-3, 3, 0.25)
x1 = np.arange(-3, 3, 0.25)

X0, X1 = np.meshgrid(x0, x1)
Y = func(X0, X1)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X0, X1, Y)
plt.show()
