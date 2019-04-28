"""
Problem ID : 2
link : https://projecteuler.net/problem=12
"""


def even_fib(N):
    seed = [1, 1]
    prev = 1
    now=1
    while now<=N:
        now, prev = prev + now, now
        if now % 2 == 0:
            yield now


def eid_2():
    """Each new term in the Fibonacci sequence is generated
    by adding the previous two terms. By starting with 1 and 2,
    the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence
    whose values do not exceed four million,
    find the sum of the even-valued terms.
    :return:
    """
    N = 4000000

    evenfib = even_fib(N)
    output = sum([val for val in evenfib])
    return output

