from all_moves.haim_special_move import HaimSpecialMove
from base_fighter import BaseFighter
import constant


class Haim(BaseFighter):
    def __init__(self):
        super(Haim, self).__init__(constant.HAIM_HP, constant.HAIM_STAMINA, constant.HAIM_STRENGTH, "Haim")

    def add_special_move(self):
        self.optional_moves.append(HaimSpecialMove())

