from model.hero import Hero

class Dwarf(Hero):
    BONUS_ENDU = 2

    def __init__(self, endurance, force, pv, current_life, x, y):
        super().__init__(endurance, force, pv, current_life, x, y)

    @property
    def endurance(self):
        return super().endurance + self.BONUS_ENDU
