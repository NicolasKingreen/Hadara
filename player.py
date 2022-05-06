from card_types import *
from epochs import *


class Player:
    def __init__(self, player_icon, setup_card):
        self.icon = player_icon
        self.setup_card = setup_card

        self.coins = setup_card.coins
        self.track_values = setup_card.track_values

        self.silver_medals = []
        self.golden_medals = []
        self.statues = []

        self.cards = {
            INCOME: [],
            MILITARY: [],
            CULTURE: [],
            FOOD: [],
            TECHNICAL: []
        }

    def add_card(self, card):
        if self.coins >= card.cost:  # make decreasing price
            if card not in self.cards[card.card_type]:
                self.cards[card.card_type].append(card)
                self.coins -= card.cost
        else:
            print("Not enough coins")

    @property
    def initiative_value(self):
        return self.setup_card.initiative_value

    def __repr__(self):
        return f"<Player({self.icon}, {self.coins} coins, {self.track_values}, {self.initiative_value}, {self.cards})>"

    def get_income(self):
        self.coins += self.track_values[INCOME]

    def has_enough_food(self):
        total_cards = sum(len(self.cards[card_type]) for card_type in self.cards)
        if total_cards >= self.track_values[FOOD]:
            random_type = random.choice(self.cards)
            random_card = random.choice(self.cards[random_type])
            self.cards[random_type].remove(random_card)


