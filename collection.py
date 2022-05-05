# constants
from card_types import *
from colony_types import *
from epochs import *

import json


from card import Card
from colony import Colony
from setup_card import SetupCard


INCOME_CARDS_PATH = "data/y_cards.json"
MILITARY_CARDS_PATH = "data/r_cards.json"
CULTURE_CARDS_PATH = "data/b_cards.json"
FOOD_CARDS_PATH = "data/g_cards.json"
TECHNICAL_CARDS_PATH = ""

COLONIES_PATH = "data/colonies.json"

SETUP_CARDS_PATH = "data/setup_cards.json"


class Collection:

    def __init__(self):

        # setup cards layout
        self.cards = {
            EPOCH1: [], 
            EPOCH2: [], 
            EPOCH3: []
        }
        for epoch in self.cards:
            self.cards[epoch] = {
                INCOME: [],
                MILITARY: [],
                CULTURE: [],
                FOOD: [],
                TECHNICAL: []
            }

        # reads cards from json
        self.load_and_add_cards(INCOME, INCOME_CARDS_PATH)
        self.load_and_add_cards(MILITARY, MILITARY_CARDS_PATH)
        self.load_and_add_cards(CULTURE, CULTURE_CARDS_PATH)
        self.load_and_add_cards(FOOD, FOOD_CARDS_PATH)

        # setup colonies layout
        self.colonies = {
            VERY_EASY: [],
            EASY: [],
            MEDIUM: [],
            HARD: [],
            VERY_HARD: []
        }

        # reads colonies from json
        with open(COLONIES_PATH) as file:
            colonies = json.load(file)
            for strength in colonies:
                for colony in colonies[strength]:
                    new_colony = Colony(int(strength), colony["values"], colony["points"])
                    self.add_colony(new_colony)

        # setting up setup cards layout
        self.setup_cards = {
            "A": [],
            "B": []
        }
        with open(SETUP_CARDS_PATH) as file:
            setup_cards = json.load(file)
            for side in setup_cards:
                for setup_card in setup_cards[side]:
                    new_setup_card = SetupCard(setup_card["initiative_value"], setup_card["coins"], setup_card["values"])
                    self.setup_cards[side].append(new_setup_card)

    def load_and_add_cards(self, cards_type, path):
        with open(path) as file:
            cards = json.load(file)
            self.add_cards_by(cards_type, cards)

    def add_cards_by(self, cards_type, cards):
        for epoch in cards:
            if epoch == "e1":
                e = EPOCH1
            elif epoch == "e2":
                e = EPOCH2
            else:
                e = EPOCH3
            for card in cards[epoch]:
                values = card["bonus"]
                # renaming json keys to type keys
                values[INCOME] = values.pop("economy")
                values[MILITARY] = values.pop("warfare")
                values[CULTURE] = values.pop("culture")
                values[FOOD] = values.pop("agriculture")
                new_card = Card(e, cards_type, values, card["victory_points"], card["cost"])
                self.add_card(new_card)

    def add_card(self, card):
        if card not in self.cards[card.epoch][card.card_type]:
            self.cards[card.epoch][card.card_type].append(card)

    def add_colony(self, colony):
        strength_to_type = {
            3: VERY_EASY,
            9: EASY,
            15: MEDIUM,
            21: HARD,
            30: VERY_HARD
        }
        colony_type = strength_to_type[colony.strength]
        self.colonies[colony_type].append(colony)

    def print(self):
        print()
        print("Cards".center(64))
        for epoch in self.cards:
            print(epoch)
            for card_type in self.cards[epoch]:
                print("\t", card_type)
                for card in self.cards[epoch][card_type]:
                    print("\t\t", card)
        print()
        print("Colonies".center(64))
        for strength in self.colonies:
            print(strength)
            for colony in self.colonies[strength]:
                print("\t", colony)
        print()
        print("Setup Cards".center(64))
        for side in self.setup_cards:
            print(side)
            for setup_card in self.setup_cards[side]:
                print("\t", setup_card)


if __name__ == "__main__":
    collection = Collection()
    collection.print()
