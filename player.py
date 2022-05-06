from card_types import *
from epochs import *
import random


class Player:
    def __init__(self, player_icon, setup_card):
        self.icon = player_icon
        self.setup_card = setup_card

        self.coins = setup_card.coins
        self.track_values = setup_card.track_values

        self.silver_medals = []
        self.golden_medals = []
        self.statues = []
        self.colonies = []

        self.cards = {
            INCOME: [],
            MILITARY: [],
            CULTURE: [],
            FOOD: [],
            TECHNICAL: []
        }

    def __repr__(self):
        return f"<Player({self.icon}, {self.coins} coins, {self.track_values}, {self.initiative_value}, {self.cards}, {self.colonies})>"

    def __str__(self):
        asterisks_line = "".join(["*" * 64, "\n"])
        base_info = f"{self.icon}. Coins: {self.coins} \n" \
                 f"({self.track_values[INCOME]}, {self.track_values[MILITARY]}, " \
                 f"{self.track_values[CULTURE]}, {self.track_values[FOOD]})\n"
        cards = "Cards:\n"
        for card_type in self.cards:
            cards += f"\t{card_type}\n"
            for card in self.cards[card_type]:
                cards += f"\t\t-> ({card.values[INCOME]}, {card.values[MILITARY]}, " \
                         f"{card.values[CULTURE]}, {card.values[FOOD]}) " \
                         f"& {card.points} victory points\n"
        colonies = "Colonies:\n"
        for colony in self.colonies:
            colonies += f"\t{colony.strength}: {colony}\n"
        return "".join([asterisks_line, base_info, cards, colonies, asterisks_line])

    @property
    def initiative_value(self):
        return self.setup_card.initiative_value

    def get_total_cards(self):
        return sum(len(self.cards[card_type]) for card_type in self.cards)

    def add_card(self, card):
        price_off = len(self.cards[card.card_type])
        if self.coins >= card.cost:
            self.cards[card.card_type].append(card)
            self.update_track_values()
            self.coins -= card.cost - price_off
            return True
        else:
            print("Not enough coins")
            return False

    def add_colony(self, colony):
        if colony not in self.colonies:
            self.colonies.append(colony)

    def update_track_values(self):
        """Recalculates track values from owned cards, colonies and sculptures"""
        track_values = self.setup_card.track_values.copy()  # initial values
        for card_type in self.cards:
            for card in self.cards[card_type]:
                for value_type in card.values:
                    track_values[value_type] += card.values[value_type]
        for colony in self.colonies:
            for value_type in colony.values:
                track_values[value_type] += colony.values[value_type]
        # TODO: count sculptures values
        self.track_values = track_values.copy()

    def get_income(self):
        self.coins += self.track_values[INCOME]

    def has_enough_food(self):
        """Checks if not sufficient food and kills overpopulation"""
        while self.get_total_cards() > self.track_values[FOOD]:
            random_type = random.choice(self.cards)
            random_card = random.choice(self.cards[random_type])
            self.cards[random_type].remove(random_card)
