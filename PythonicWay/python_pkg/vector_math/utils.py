# utils.py
import math

def normalize(vector):
    mag = magnitude(vector)
    if mag == 0:
        raise ValueError("Cannot normalize a zero vector")
    return vector * (1 / mag)

def magnitude(vector):
    return math.sqrt(sum(member ** 2 for member in vector.members))
