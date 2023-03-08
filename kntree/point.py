class Point:
    def __init__(self, *coord) -> None:
        for i in coord:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise SyntaxError("Not a vaild point")
        if len(coord) == 0:
            raise SyntaxError("Not a vaild point")
        self.point = coord
        self.dimension = len(self.point)

    def __repr__(self):
        if self.dimension >= 2:
            return str(self.point)
        else:
            return str(self.point[0])

    def __getitem__(self, key):
        return self.point[key]
