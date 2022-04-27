from all_moves.rahamim_special_move import RahamimSpecialMove
from base_fighter import BaseFighter


class Rahamim(BaseFighter):

    def __init__(self):
        super(Rahamim, self).__init__(25, 14, 4, "Rahamim")

    def add_special_move(self, ):
        self.optional_moves.append(RahamimSpecialMove())
        print("AAAAAAAAAAAAAAAA")
