from enum import IntEnum


class ValueType(IntEnum):
    INCOME = 1
    MILITARY = 2
    CULTURE = 3
    FOOD = 4


class CardType(IntEnum):
    DUMMY = 0
    INCOME = 1
    MILITARY = 2
    CULTURE = 3
    FOOD = 4
    TECHNICAL = 5


class ColonyType(IntEnum):
    DUMMY = 0
    VERY_EASY = 3
    EASY = 9
    MEDIUM = 15
    HARD = 21
    VERY_HARD = 30


class SculptureType(IntEnum):
    TINY = 6
    SMALL = 12
    REGULAR = 20
    HUGE = 30
