"""
Problem ID : 81
link : https://projecteuler.net/problem=81
"""

def design_path(i1, j1, i2, j2):
    i, j = i1, j1
    while i1 != i2 and j1


def eid_081():
    """link : https://projecteuler.net/problem=81
    [1 2 3 4 5]
    [11 22 33 44 55]
    [111 222 333 444 555]

    [1,1] ------ > [3,3]
    down(i, j) --> (i+1,j)
    right(i, j) --> (i, j+1)

    """

    import numpy as np

    arr = np.loadtxt('./temp/p081_matrix.txt', delimiter=',')
    init = 1

    i, j = init, init


