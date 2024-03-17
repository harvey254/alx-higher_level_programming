#!/usr/bin/python3
def pow(a, b):
    # Base case: if exponent is 0, result is 1
    if b == 0:
        return 1
    # Base case: if exponent is 1, result is the base
    if b == 1:
        return a

    # For negative exponents, compute the reciprocal of the base raised to the positive exponent
    if b < 0:
        a = 1 / a
        b = -b

    result = 1
    # Multiply the base by itself b times
    for _ in range(b):
        result *= a

    return result
