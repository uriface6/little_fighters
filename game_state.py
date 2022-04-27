from player import Player
from typing import List


class GameState:
    def __init__(self, players: List[Player], curr_player: Player):
        self.players = players
        self.curr_player = curr_player
