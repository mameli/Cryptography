import math


def euclideEsteso(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    bStart = b
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - quotient * x1
        y0, y1 = y1, y0 - quotient * y1
    return (a, x0, y0) if a != 1 else (a, x0, y0, x0 % bStart)

# print euclideEsteso(17, 60)