from abc import ABC, abstractmethod
from model.dice import Dice

class Character:
    def __init__(self, endurance, force, pv, current_life, x, y):
        self.__endurance = endurance
        self.__force = force
        self.__pv = pv
        self.__current_life = current_life
        self.__x = x
        self.__y = y

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @property
    def force(self):
        return self.__force

    @force.setter
    def force(self, value):
        self.__force = value

    @property
    def pv(self):
        return self.__pv

    @pv.setter
    def pv(self, value):
        self.__pv = value

    @property
    def current_life(self):
        return self.__current_life

    @current_life.setter
    def current_life(self, value):
        self.__current_life = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


    def hit(self, foe: Character, dice: Dice):
        result = dice.roll()
        result += self.calculer_bonus(self.force)
        foe.submit_damages(result)

    def is_alive(self):
        return self.current_life > 0
    
    def submit_damages(self, damages):
        self.current_life = self.current_life - damages

    @staticmethod
    def calculer_bonus(value):
        if value < 5:
            return -1
        elif value < 10:
            return  0
        elif value < 15:
            return 1
        
        return 2

# 
# Character_on_map(get_x(), get_y())
# [Character, pv, pos, gold, leather]
# > Character[Endu, Force, pv] ( hit )
# > pos (move_up, move_right, move_down, move_left)
# > bag [gold, leather] (take_all, take_one, list_bag, add_one)
# > life [pv] (restore_all, suffer_damage, heal)
# > map 
# Monster, life, 
# Human
# Dwarf








