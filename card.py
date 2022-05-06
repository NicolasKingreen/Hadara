from card_types import *


class Card:
    def __init__(self, epoch, card_type, values, points, cost, effect=None):
        self.epoch = epoch
        self.card_type = card_type
        self.values = values
        self.points = points
        self.cost = cost
        self.effect = effect

    def __repr__(self):
        return f"<Card({self.epoch}, {self.card_type}, {self.values}, {self.points}, {self.cost}, {self.effect})>"

    def __str__(self):
        return f"{self.card_type} ({self.epoch}) Price: {self.cost}\n" \
               f"({self.values[INCOME]}, {self.values[MILITARY]}, " \
               f"{self.values[CULTURE]}, {self.values[FOOD]})\n" \
               f"Victory points: {self.points}"

