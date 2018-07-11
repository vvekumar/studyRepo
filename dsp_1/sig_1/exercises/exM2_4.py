# ex. M2.4 (SKM)
import numpy as np
import matplotlib.pyplot as plt

class Error(Exception):
    pass

def generate_plot_sinusoid(L, A, w0, phi):
    '''Generate a sinusoid given values for 
    L(length in num samples)
    A(gain)
    w0(normalized desired angular frequency)
    phi(phase)'''
    # x(n) = A*cos(w0n + phi)
    if not (phi >= 0 and phi <= 2*np.pi) :
        raise ValueError('Value of phi must be in [0, 2*pi]')
    if not (w0 >= 0 and phi <= np.pi) :
        raise ValueError('Value of phi must be in [0, pi]')
        
    n = np.arange(0,L,1)
    x = A*np.cos(w0*n + phi)
    
    # Plot
    plt.figure()
    plt.stem(n, x)
    plt.xlabel('time index')
    plt.ylabel('amplitude')
    plt.grid()
    plt.title('Sinusoidal Signal : %s*cos(%.2f*n + %.2f)' %(A, w0, phi))
    plt.show()
    
    
# Test
A = 2
L = 40
w0 = 1.8*np.pi
phi = 0
generate_plot_sinusoid(L, A, w0, phi)