from model.monster import Monster
from model.dice import Dice
from model.loot_interface import LootInterface

class Orc(Monster, LootInterface):
    def __init__(self, endurance, force, pv, current_life, x, y):
        super().__init__(endurance, force, pv, current_life, x, y)
        self.__gold = Dice.DICE_SIX.roll()

    @property
    def gold(self):
        return self.__gold
    
    def loot(self):
        if self.__gold <= 0:
            raise ValueError()
        
        loot = self.gold
        self.__gold = 0
        return loot

