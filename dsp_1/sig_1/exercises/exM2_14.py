# ex. M2.14 (SKM)
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

class Error(Exception):
    pass


def generate_random_sinusoid(L, w0):
    '''
    Create a random signal with uniform distrbution (0,4) for Amplitude
    (0,2*pi) for phase'''
    # x(n) = A*cos(w0n + phi)
    
    """
    if not (phi >= 0 and phi <= 2*np.pi) :
        raise ValueError('Value of phi must be in [0, 2*pi]')
    if not (w0 >= 0 and phi <= np.pi) :
        raise ValueError('Value of phi must be in [0, pi]')
    """
    phi = rand.uniform(0, 2*np.pi)
    A = rand.uniform(0, 4)
        
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
# A = 2
L = 40
w0 = 0.14*np.pi
# phi = 0
generate_random_sinusoid(L, w0)