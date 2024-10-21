# Example usage:
# from vector_math import Vector, Matrix, dot_product, cross_product, normalize, magnitude
from vector_math.vector import Vector
from vector_math.matrix import Matrix
from vector_math.operations import dot_product, cross_product
from vector_math.utils import normalize, magnitude

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print("Vector Addition: ", v1 + v2)
print("Dot Product: ", dot_product(v1, v2))
print("Cross Product: ", cross_product(v1, v2))
print("Normalize: ", normalize(v1))
print("Magnitude: ", magnitude(v1))

m1 = Matrix([1, 2], [3, 4])
m2 = Matrix([5, 6], [7, 8])
print(m1 * m2)