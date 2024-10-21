# operations.py
from .vector import Vector

def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    return sum(a * b for a, b in zip(v1.members, v2.members))

def cross_product(v1, v2):
    if len(v1.members) != 3 or len(v2.members) != 3:
        raise ValueError("Cross product is only defined for 3D vectors")
    a1, a2, a3 = v1.members
    b1, b2, b3 = v2.members
    return Vector(
        a2 * b3 - a3 * b2,
        a3 * b1 - a1 * b3,
        a1 * b2 - a2 * b1
    )
