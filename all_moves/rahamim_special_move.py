# from game_state import GameState
from base_move import BaseMove
import constant


class RahamimSpecialMove(BaseMove):

    def __init__(self):
        super(RahamimSpecialMove, self).__init__("make equal hp", constant.MoveType.DUEL_MOVE)

    def play_move(self, my_game_state: "GameState"):
        victim = self.parameters[0]
        print(f"{my_game_state.curr_player.name} make equal hp to {victim.name}")

        print("victim before move:")
        print(victim)
        victim.fighter.hp = my_game_state.curr_player.fighter.hp
        print("victim after move:")
        print(victim)
