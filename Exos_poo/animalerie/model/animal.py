from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, weight, height, sex, age, human_age):
        pass

    
    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def get_death_probability():
        pass


