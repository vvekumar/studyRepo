# ex. M2.1, M2.2, M2.3
'''
Purpose : Helper functions for creating test sequences
'''
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt


class Error(Exception):
    pass

def plotter(x, y, _title, _type='stem'):
    plt.close()
    fig = plt.figure()
    if _type == 'stem':
        plt.stem(x, y)
    elif _type == 'simple':
        plt.plot(x, y)
    plt.title(_title)
    plt.show()
    return fig

def dirac(n_init, L, Fs, is_plot = True):
    n = np.arange(n_init, L*1/Fs, 1/Fs)   
    seq = [1 if i==0 else 0 for i in n ]
    if is_plot is True:
        fig = plotter(n, seq, 'dirac')
    return seq

# Test
#n = range(-20, 40)
#x = dirac(n)

def step(n_init, L, Fs, is_plot = True):
    n = np.arange(n_init, L*1/Fs, 1/Fs)
    seq = [1 if i > 0 else 0 for i in n]
    if is_plot is True:
        fig = plotter(n, seq, 'step')
    return seq


def ramp(n_init, L, Fs, is_plot = True):
    n = np.arange(n_init, L*1/Fs, 1/Fs)
    seq = [i if i >= 0 else 0 for i in n]
    if is_plot is True :
         fig = plotter(n, seq, 'ramp')
    return seq

# Test
# n = range(-20, 40)




n_init = 0
L = 100
Fs = 20000
x = dirac(n_init, L, Fs)
x2 = step(n_init, L, Fs)
x3 = ramp(n_init, L, Fs)