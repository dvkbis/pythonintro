from model.hero import Hero
from model.monster import Monster
from model.dice import Dice

class Combat:
    def __init__(self, hero, monster):
        self.__hero = hero
        self.__monster = monster
        self.__round = 0
        self.__infos_combat = []

    def is_over(self) -> bool:
        return not self.__hero.is_alive() or not self.__monster.is_alive()
    
    def next_combat(self):
        if self.is_over(): return None

        if self.__round % 2:
            self.__hero.hit(self.__monster, Dice.DICE_FOUR)
        else:
            self.__monster.hit(self.__hero, Dice.DICE_FOUR)
        
        self.__round += 1
        print(f"ROUND {self.__round} || Hero: {self.__hero.current_life} || Monster: {self.__monster.current_life}")

