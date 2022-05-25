# from game_state import GameState
from base_move import BaseMove
import constant


class PikatzuSpecialMove(BaseMove):

    def __init__(self):
        super(PikatzuSpecialMove, self).__init__("electrocuted everybody", constant.MoveType.WITHOUT_ME_MOVE)

    def play_move(self, my_game_state: "GameState"):
        print(f"{my_game_state.curr_player.name} electrocuted everybody")

        print("before move:")
        for victim_player in self.parameters:
            print(victim_player)
            victim_player.fighter.hp -= 10

        print("after move:")
        for victim_player in self.parameters:
            print(victim_player)
