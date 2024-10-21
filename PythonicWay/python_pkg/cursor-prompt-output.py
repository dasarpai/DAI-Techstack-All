# # Vector Mathematics Package Structure

# # Folder structure:
# # vector_math/
# # ├── __init__.py
# # ├── vector.py
# # ├── matrix.py
# # ├── operations.py
# # └── utils.py

# # Contents of each file:

# # __init__.py
# from .vector import Vector
# from .matrix import Matrix
# from .operations import dot_product, cross_product
# from .utils import normalize, magnitude

# # vector.py
# class Vector:
#     def __init__(self, *components):
#         self.components = list(components)

#     def __repr__(self):
#         return f"Vector({', '.join(map(str, self.components))})"

#     def __add__(self, other):
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must have the same dimension")
#         return Vector(*[a + b for a, b in zip(self.components, other.components)])

#     def __sub__(self, other):
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must have the same dimension")
#         return Vector(*[a - b for a, b in zip(self.components, other.components)])

#     def __mul__(self, scalar):
#         return Vector(*[component * scalar for component in self.components])

# # matrix.py
# class Matrix:
#     def __init__(self, *rows):
#         self.rows = rows
#         self.columns = list(zip(*rows))

#     def __repr__(self):
#         return f"Matrix({self.rows})"

#     def __add__(self, other):
#         if len(self.rows) != len(other.rows) or len(self.columns) != len(other.columns):
#             raise ValueError("Matrices must have the same dimensions")
#         return Matrix(*[[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, other.rows)])

#     def __mul__(self, other):
#         if isinstance(other, Matrix):
#             if len(self.columns) != len(other.rows):
#                 raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
#             return Matrix(*[[sum(a * b for a, b in zip(row, col)) for col in other.columns] for row in self.rows])
#         elif isinstance(other, (int, float)):
#             return Matrix(*[[element * other for element in row] for row in self.rows])

# # operations.py
# def dot_product(v1, v2):
#     if len(v1.components) != len(v2.components):
#         raise ValueError("Vectors must have the same dimension")
#     return sum(a * b for a, b in zip(v1.components, v2.components))

# def cross_product(v1, v2):
#     if len(v1.components) != 3 or len(v2.components) != 3:
#         raise ValueError("Cross product is only defined for 3D vectors")
#     a1, a2, a3 = v1.components
#     b1, b2, b3 = v2.components
#     return Vector(
#         a2 * b3 - a3 * b2,
#         a3 * b1 - a1 * b3,
#         a1 * b2 - a2 * b1
#     )

# # utils.py
# import math

# def normalize(vector):
#     mag = magnitude(vector)
#     if mag == 0:
#         raise ValueError("Cannot normalize a zero vector")
#     return vector * (1 / mag)

# def magnitude(vector):
#     return math.sqrt(sum(component ** 2 for component in vector.components))

# # Example usage:
# # from vector_math import Vector, Matrix, dot_product, cross_product, normalize, magnitude

# # v1 = Vector(1, 2, 3)
# # v2 = Vector(4, 5, 6)
# # print(v1 + v2)
# # print(dot_product(v1, v2))
# # print(cross_product(v1, v2))
# # print(normalize(v1))
# # print(magnitude(v1))

# # m1 = Matrix([1, 2], [3, 4])
# # m2 = Matrix([5, 6], [7, 8])
# # print(m1 * m2)
