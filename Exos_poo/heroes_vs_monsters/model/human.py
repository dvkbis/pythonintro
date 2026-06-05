from hero import Hero

class Human(Hero):
    BONUS_FORCE = 1
    BONUS_ENDU = 1
    def __init__(self, endurance, force, pv, current_life, x, y):
        super().__init__(endurance, force, pv, current_life, x, y)

    @property
    def force(self):
        return super().force + self.BONUS_FORCE
    
    @property
    def endurance(self):
        return super().endurance + self.BONUS_ENDU
    


