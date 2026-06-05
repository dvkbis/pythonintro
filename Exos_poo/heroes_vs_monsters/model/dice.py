from random import randint
from enum import Enum

class Dice(Enum):
    DICE_THREE = 3
    DICE_FOUR = 4
    DICE_SIX = 6

    def roll(self):
        return randint(1, self.value)
    
    def roll_best(self, n_rolls, n_best):
        rolls = [self.roll() for _ in range(n_rolls)]
        rolls.sort(reverse=True)
        return rolls[:n_best]


