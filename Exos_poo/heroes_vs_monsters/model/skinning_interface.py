from abc import ABC, abstractmethod

class SkinningInterface(ABC):
    @abstractmethod
    def skinning(self):
        pass