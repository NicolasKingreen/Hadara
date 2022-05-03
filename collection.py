from card_types import *
from epochs import *

from resourses import CARDS
from card import Card


class Collection:

    def __init__(self):

        # cards
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

        # loading
        for epoch in CARDS:
            for card_type in CARDS[epoch]:
                card_data = CARDS[epoch][card_type]
                if card_data:
                    self.add_card(Card(epoch, card_type, *card_data[0]))

        # colonies
        self.very_easy_colonies = []
        self.easy_colonies = []
        self.medium_colonies = []
        self.hard_colonies = []
        self.very_hard_colonies = []
        
    def add_card(self, card):
        if card not in self.cards[card.epoch][card.card_type]:
            self.cards[card.epoch][card.card_type].append(card)

    def add_colony(self, colony):
        if colony.strength == 3:
            self.very_easy_colonies.append(colony)
        elif colony.strength == 9:
            self.easy_colonies.append(colony)
        elif colony.strength == 15:
            self.medium_colonies.append(colony)
        elif colony.strength == 21:
            self.hard_colonies.append(colony)
        elif colony.strength == 30:
            self.very_hard_colonies.append(colony)


collection = Collection()
print(collection.cards)
