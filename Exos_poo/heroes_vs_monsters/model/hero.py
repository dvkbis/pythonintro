from abc import ABC, abstractmethod
from character import Character

class Hero(ABC, Character):
    def __init__(self, endurance, force, pv, current_life, x, y):
        super().__init__(endurance, force, pv, current_life, x, y)
        self.__leather = 0
        self.__gold = 0

    ## GETTER / SETTER
    @property
    def leather(self):
        return self.__leather
    
    @leather.setter
    def leather(self, leather):
        self.__leather = leather

    @property
    def gold(self):
        return self.__gold
    
    @gold.setter
    def gold(self, gold):
        self.__gold = gold

    def regenerate(self):
        self.current_life = self.pv

    def get_description(self):
        return f"(endu= {self.endurance}, force= {self.force}, pv= {self.pv})"

    