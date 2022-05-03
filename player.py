from card_types import *
from epochs import *


class Player:
    def __init__(self, setup_card):
        self.flag = FLAGS[0]
        self.money = 10
        self.stats = {
                "wealth": 1,
                "military": 1,
                "culture": 1,
                "food": 1
        }
        self.silver_medals = []
        self.golden_medals = []
        self.statues = []
        self.cards = {
            WEALTH: [],
            MILITARY: [],
            CULTURE: [],
            FOOD: [],
            TECHNICAL: []
        }

