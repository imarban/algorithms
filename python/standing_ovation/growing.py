from decimal import Decimal
from math import factorial

__author__ = 'igomez'


def going(n):
    denom = 1
    numer = 0
    for i in range(1, n + 1):
        denom *= i
        numer += denom
    return (1000000 * numer / denom) / 1000000.0


def going(n):
    suma = long(sum([factorial(i) for i in range(1, n + 1)]))
    den = long(factorial(n))

    return (1000000 * suma / den) / 1000000.0


print going(5)
