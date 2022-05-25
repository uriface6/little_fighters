from all_moves.LitalSpecialMove import LitalSpecialMove
from base_fighter import BaseFighter
import constant


class Lital(BaseFighter):
    def __init__(self):
        super(Lital, self).__init__(constant.LITAL_HP, constant.LITAL_STAMINA, constant.LITAL_STRENGTH, "Lital")

    def add_special_move(self):
        self.optional_moves.append(LitalSpecialMove())
