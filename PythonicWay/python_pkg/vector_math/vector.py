# vector.py
class Vector:
    def __init__(self, *members):
        self.members = list(members)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.members))})"

    def __add__(self, other):
        if len(self.members) != len(other.members):
            raise ValueError("Vectors must have the same dimension")
        return Vector(*[a + b for a, b in zip(self.members, other.members)])

    def __sub__(self, other):
        if len(self.members) != len(other.members):
            raise ValueError("Vectors must have the same dimension")
        return Vector(*[a - b for a, b in zip(self.members, other.members)])

    def __mul__(self, scalar):
        return Vector(*[component * scalar for component in self.members])

    def __getitem__(self, index):
        return self.members[index]

    def __len__(self):
        return len(self.members)
