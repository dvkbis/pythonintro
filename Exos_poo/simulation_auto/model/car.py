from random import randint
class Car:

    def __init__(self, name, min_speed, max_speed):
        self.name = name
        self.__min_speed = min_speed
        self.__max_speed = max_speed
    
    @property
    def min_speed(self):
        return self.__min_speed
    
    @property
    def max_speed(self):
        return self.__max_speed
    
    def __str__(self):
        return f"{self.name}  ({self.__min_speed} - {self.__max_speed})" 
    
    def __repr__(self):
        return self.__str__()
    
    def simulate_speed(self):
        return randint(self.__min_speed, self.__max_speed)
