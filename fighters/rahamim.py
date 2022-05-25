from all_moves.rahamim_special_move import RahamimSpecialMove
from base_fighter import BaseFighter
import constant


class Rahamim(BaseFighter):

    def __init__(self):
        super(Rahamim, self).__init__(constant.RAHAMIM_HP, constant.RAHAMIM_STAMINA, constant.RAHAMIM_STRENGTH, "Rahamim")

    def add_special_move(self, ):
        self.optional_moves.append(RahamimSpecialMove())
