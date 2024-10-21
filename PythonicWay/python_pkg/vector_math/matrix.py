# matrix.py
class Matrix:
    def __init__(self, *rows):
        self.rows = rows
        self.columns = list(zip(*rows))

    def __repr__(self):
        return f"Matrix({self.rows})"

    def __add__(self, other):
        if len(self.rows) != len(other.rows) or len(self.columns) != len(other.columns):
            raise ValueError("Matrices must have the same dimensions")
        return Matrix(*[[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, other.rows)])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if len(self.columns) != len(other.rows):
                raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
            return Matrix(*[[sum(a * b for a, b in zip(row, col)) for col in other.columns] for row in self.rows])
        elif isinstance(other, (int, float)):
            return Matrix(*[[element * other for element in row] for row in self.rows])
