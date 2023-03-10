class Vector:
    def __init__(self, *coords):
        if len(coords) > 1:
            self.vector = coords
        else:
            raise ValueError("Not a valid vector")

    def __add__(self, other):
        if (len(self.vector) != len(other.vector)):
            raise ValueError(
                "Can't resolve add between two vectors of different dimensions")
        else:
            temp_result = list()
            for i in range(len(self.vector)):
                temp_result.append(self.vector[i] + other.vector[i])
            return Vector(tuple(temp_result))

    def __sub__(self, other):
        if (len(self.vector) != len(other.vector)):
            raise ValueError(
                "Can't resolve minus between two vectors of different dimensions")
        else:
            temp_result = list()
            for i in range(len(self.vector)):
                temp_result.append(self.vector[i] - other.vector[i])
            return Vector(tuple(temp_result))

    def __mul__(self, other):
        if isinstance(other, Vector):
            result = 0
            if (len(self.vector) != len(other.vector)):
                raise ValueError(
                    "Can't resolve dot product between two vectors of different dimensions")
            else:
                for i in range(len(self.vector)):
                    result += self.vector[i] * other.vector[i]
                return result
        if (isinstance(other, int) or isinstance(other, float)):
            temp_result = list()
            for i in range(len(self.vector)):
                temp_result.append(self.vector[i] * other)
            return Vector(tuple(temp_result))

    def __rmul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            temp_result = list()
            for i in range(len(self.vector)):
                temp_result.append(self.vector[i] * other)
            return Vector(tuple(temp_result))

    def __repr__(self):
        repr = "("
        for i in range(len(self.vector)):
            if (repr == "("):
                repr += str(self.vector[i])
            else:
                repr += f", {str(self.vector[i])}"
        repr += ')'
        return repr
    
    def __len__(self):
        return len(self.vector)
    
    def __getitem__(self, key):
        return self.vector[key]
