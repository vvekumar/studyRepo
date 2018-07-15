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

<<<<<<< HEAD
def prdc_square(n_init, pk_val, L, duty_cycle_pc, T, Fs, is_plot = True):
    n = np.arange(n_init, L*1/Fs, 1/Fs)
    seq = [ pk_val*1 if (idx % T) <= duty_cycle_pc*T else -1*pk_val for idx, i in enumerate(n) ]
    if is_plot is True :
         fig = plotter(n, seq, 'ramp')
    return seq    


def prdc_sawtooth(n_init, pk_val, L, T, Fs, is_plot = True):
    
    seq0 = [ pk_val * (idx % T)/T for idx in range(L) ]
    seq = [ val - (pk_val /2) for val in seq0 ]
    if is_plot is True :
         fig = plotter(range(L), seq, 'sawtooth')
    return seq    

# Test
n_init = 0
L = 100
Fs = 20000
pk_val = 7
T = 13

duty_cycle_pc = .6
# prdc_square(n_init, pk_val, L, duty_cycle_pc, T, Fs)
x5 = prdc_sawtooth(n_init, pk_val, L, T, Fs)
=======
# Test
# n = range(-20, 40)




n_init = 0
L = 100
Fs = 20000
x = dirac(n_init, L, Fs)
x2 = step(n_init, L, Fs)
x3 = ramp(n_init, L, Fs)
>>>>>>> 593eaee93cb26dd4a4c82e354d643c1ae00ba9e5
