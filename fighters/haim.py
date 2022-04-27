from base_fighter import BaseFighter


class Haim(BaseFighter):
    def __init__(self):
        super().__init__(100, 3, 2, "Haim")

    def special_move(self):
        """i am Haim attack"""

