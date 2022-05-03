class Card:
    def __init__(self, epoch, card_type, values, points, cost, effect=None):
        self.epoch = epoch
        self.card_type = card_type
        self.values = values
        self.points = points
        self.cost = cost
        self.effect = effect

