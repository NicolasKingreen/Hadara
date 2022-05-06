from card_types import *


class Colony:
    def __init__(self, strength, values, points):
        self.strength = strength
        self.points = points
        self.values = values

    def __repr__(self):
        return f"<Colony({self.strength}, {self.points}, {self.values})>"

    def __str__(self):
        return f"({self.values[INCOME]}, {self.values[MILITARY]}," \
               f"{self.values[CULTURE]}, {self.values[FOOD]}) " \
               f"& {self.points} victory points"
