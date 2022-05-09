# system
import random
import json
# constants
from epochs import *
from card_types import *
from colony_types import *
from structure_types import *
# classes
from card import Card
from colony import Colony
from setup_card import SetupCard
from statue import Statue


INCOME_CARDS_PATH = "data/y_cards.json"
MILITARY_CARDS_PATH = "data/r_cards.json"
CULTURE_CARDS_PATH = "data/b_cards.json"
FOOD_CARDS_PATH = "data/g_cards.json"
TECHNICAL_CARDS_PATH = ""

SETUP_CARDS_PATH = "data/setup_cards.json"
COLONIES_PATH = "data/colonies.json"
STATUES_PATH = "data/statues.json"


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

        # setting up setup cards layout
        self.setup_cards = {
            "A": [],
            "B": []
        }
        with open(SETUP_CARDS_PATH) as file:
            setup_cards = json.load(file)
            for side in setup_cards:
                for setup_card in setup_cards[side]:
                    new_setup_card = SetupCard(setup_card["initiative_value"],
                                               setup_card["coins"],
                                               setup_card["values"])
                    self.setup_cards[side].append(new_setup_card)

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

        # statues
        self.statues = {
            TINY: None,
            SMALL: None,
            REGULAR: None,
            HUGE: None
        }

        with open(STATUES_PATH) as file:
            statues = json.load(file)
            for statue_requirement in statues:
                new_statue = Statue(int(statue_requirement),
                                    statues[statue_requirement]['Counter'],
                                    statues[statue_requirement]['Victory points'])
                self.add_statue(new_statue)

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

    def remove_card(self, card):
        if card in self.cards[card.epoch][card.card_type]:
            self.cards[card.epoch][card.card_type].remove(card)

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

    def add_statue(self, statue):
        requirement_to_type = {
            6: TINY,
            12: SMALL,
            20: REGULAR,
            30: HUGE
        }
        statue_type = requirement_to_type[statue.culture]
        self.statues[statue_type] = statue

    def set_for_n_players(self, n):
        for epoch in self.cards:
            for card_type in self.cards[epoch]:
                for _ in range(len(self.cards[epoch][card_type]) - n * 2):
                    self.cards[epoch][card_type].remove(random.choice(self.cards[epoch][card_type]))

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

        print()
        print(self.statues)


if __name__ == "__main__":
    collection = Collection()
    collection.print()
