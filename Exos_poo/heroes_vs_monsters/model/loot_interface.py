from abc import ABC, abstractmethod

class LootInterface(ABC):
    
    @abstractmethod
    def loot(self):
        pass