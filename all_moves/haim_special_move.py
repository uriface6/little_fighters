# from game_state import GameState
from base_move import BaseMove
import constant


class HaimSpecialMove(BaseMove):

    def __init__(self):
        super(HaimSpecialMove, self).__init__("double stamina", constant.MoveType.SINGLE_MOVE)

    def play_move(self, my_game_state: "GameState"):
        print(f"{my_game_state.curr_player.name} double his stamina")

        print("before move:")
        print(my_game_state.curr_player)
        my_game_state.curr_player.fighter.stamina *= 2
        print("after move:")
        print(my_game_state.curr_player)
