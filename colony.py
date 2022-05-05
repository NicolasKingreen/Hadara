class Colony:
    def __init__(self, strength, values, points):
        self.strength = strength
        self.points = points
        self.values = values

    def __repr__(self):
        return f"<Colony({self.strength}, {self.points}, {self.values})>"
