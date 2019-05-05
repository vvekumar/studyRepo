"""
Problem ID : 81
link : https://projecteuler.net/problem=81
"""

import numpy as np


def paths(row1, col1, row2, col2):
    num_right = col2 - col1
    num_down = row2 - row1
    return [num_right, num_down]  if num_right >= 0 and num_down >= 0 else [ None, None]


def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]


class Node:
    # MATRIX_FILE='./temp/example_p081_matrix.txt'
    MATRIX_FILE = './temp/p081_matrix.txt'
    matrix = np.loadtxt(MATRIX_FILE, delimiter=',')

    def __init__(self, row, column, matrix=matrix):
        self.row = row
        self.column = column
        self.val = self.get_val()
        self.matrix = matrix

    def down(self):
        return Node(self.row+1, self.column)

    def right(self):
        return Node(self.row, self.column+1)

    def get_val(self):
        return self.matrix[self.row, self.column]


def find_cost(_path):
     cost = 0

     row, col = 0, 0
     node = Node(row, col)
     for elem in _path:
        cost += node.val
        if elem == 1:
            # Down
            node = node.down()
        else:
            # Right
            node = node.right()
     cost += node.val
     return cost


def eid_081():
    """link : https://projecteuler.net/problem=81
    [1 2 3 4 5]
    [11 22 33 44 55]
    [111 222 333 444 555]

    [1,1] ------ > [3,3]
    down(i, j) --> (i+1,j)
    right(i, j) --> (i, j+1)

    """
    strt_i, strt_j = 0, 0
    end_i, end_j = 79, 79

    num_right, num_left = paths(strt_i, strt_j, end_i, end_j)


    # 1 ==> Down
    # 0 ==> Right

    path_template = np.zeros( (2*(end_i - strt_i),), dtype=int )
    for i in range(num_right):
        path_template[i] = 1

    # 1 ==> Down
    # 0 ==> Right
    path_template = np.ndarray.tolist(path_template)
    all_paths = permute(path_template)
    arr_path_cost = []

    idx = 0
    for path in all_paths:
        idx+=1
        cost = find_cost(path)
        arr_path_cost.append(cost)

    return min(arr_path_cost), "num paths:", len(arr_path_cost)