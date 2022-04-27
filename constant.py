from enum import Enum


MIN_PLAYERS = 2
MAX_PLAYERS = 4

DEFENSE_PRISE = 3

FIGHTERS_DICT = {
    "Haim": (100, 3, 2),
    "Rahamim": (25, 14, 4),
    "Field Barvaz": (70, 6, 3),
    "Lital": (50, 8, 3)
}
MOVES_DICT = {
    "Kamkiza": 1,
    "Attack": 2,
    "Defense": 3,
}


class MoveType(Enum):
    SINGLE_MOVE = 0
    DUEL_MOVE = 1
    GENERAL_MOVE = 2
    WITHOUT_ME_MOVE = 3

