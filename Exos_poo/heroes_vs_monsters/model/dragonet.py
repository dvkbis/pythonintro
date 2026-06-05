from model.skinning_interface import SkinningInterface
from model.loot_interface import LootInterface
from model.monster import Monster
from model.dice import Dice

class Dragonet(Monster, SkinningInterface, LootInterface):
    def __init__(self, endurance, force, pv, current_life, x, y):
        super().__init__(endurance, force, pv, current_life, x, y)
        self.__leather = Dice.DICE_SIX.roll()
        self.__gold = Dice.DICE_SIX.roll()

    ## GETTER / SETTER
    @property
    def leather(self):
        return self.__leather
    
    @property
    def gold(self):
        return self.__gold
    

    ### OVERRIDE METHODS

    def loot(self):
        if self.__gold <= 0:
            raise ValueError()
        
        loot = self.gold
        self.__gold = 0
        return loot
    
    def skinning(self):
        if self.__leather <= 0:
            raise ValueError()
        
        leather = self.leather
        self.__leather = 0
        return leather

