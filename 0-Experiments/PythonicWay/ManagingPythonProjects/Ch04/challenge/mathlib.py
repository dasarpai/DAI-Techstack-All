"""A simple math library"""


def sqrt(n, epsilon=0.0001):
    """Compute square root of n using Newton's method"""
    if n < 0:
        raise ValueError('n must be >= 0 (got {})'.format(n))

    # Fast path
    if n in (0, 1):
        return n

    guess = 1.0
    while abs(guess*guess - n) > epsilon:
        guess = (n / guess + guess) / 2.0

    return guess
