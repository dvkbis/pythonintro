from skinning_interface import SkinningInterface
from monster import Monster
from dice import Dice

class Wolf(Monster, SkinningInterface):
    def __init__(self, endurance, force, pv, current_life, x, y):
        super().__init__(endurance, force, pv, current_life, x, y)
        self.__leather = Dice.DICE_SIX.roll()

    ## GETTER / SETTER
    @property
    def leather(self):
        return self.__leather

    ### OVERRIDE METHODS
    def skinning(self):
        if self.__leather <= 0:
            raise ValueError()
        
        leather = self.leather
        self.__leather = 0
        return leather

