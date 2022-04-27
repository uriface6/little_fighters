# from game_state import GameState
from base_move import BaseMove
import constant


class Defense(BaseMove):

    def __init__(self):
        super(Defense, self).__init__("Defense", constant.MoveType.SINGLE_MOVE)

    def play_move(self, my_game_state: "GameState"):
        print(f"{my_game_state.curr_player.name} is protected")
        my_game_state.curr_player.fighter.safe = True
        my_game_state.curr_player.fighter.stamina -= constant.DEFENSE_PRISE
