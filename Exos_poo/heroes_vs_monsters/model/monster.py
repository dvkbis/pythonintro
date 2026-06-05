from character import Character
from abc import ABC

class Monster(ABC, Character):

    def __init__(self, endurance, force, pv, current_life, x, y):
        super().__init__(endurance, force, pv, current_life, x, y)


    
