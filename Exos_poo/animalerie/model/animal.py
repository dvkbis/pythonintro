from abc import ABC, abstractmethod
from enum import Enum
from datetime import date
import random


class Gender(Enum):
    FEMALE = "F"
    MALE = "M"

class Animal(ABC):

    # Constructor
    def __init__(
        self,
        name: str,
        weight: float,
        size: float,
        gender: Gender,
        age: int
    ):
        self._name = name
        self._weight = weight
        self._size = size
        self._gender = gender
        self._age = age
        self._arrival_date = date.today()
        self._dead = False

    # =========================
    # Getters / Setters
    # =========================

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def arrival_date(self):
        return self._arrival_date

    @property
    def is_dead(self):
        return self._dead

    # =========================
    # Abstract methods
    # =========================

    @abstractmethod
    def death_probability(self) -> float:
        pass

    @abstractmethod
    def make_sound(self) -> str:
        pass

    # =========================
    # Utility methods
    # =========================

    def get_description(self) -> str:
        return (
            f"{self.name}, "
            f"weight: {self.weight} kg, "
            f"size: {self.size} cm, "
            f"gender: {self.gender.value}, "
            f"age: {self.age}"
        )

    def pass_day(self):
        if self.is_dead:
            raise RuntimeError("Uh... it's dead!")

    def die(self):
        self._dead = True

    def pass_night(self):
        if self.is_dead:
            raise RuntimeError("Uh... it's dead!")

        probability = random.uniform(0, 100)

        if probability < self.death_probability():
            self.die()

    # =========================
    # String representation
    # =========================

    def __str__(self):
        return (
            f"Animal("
            f"name='{self._name}', "
            f"weight={self._weight}, "
            f"size={self._size}, "
            f"gender={self._gender}, "
            f"age={self._age}, "
            f"arrival_date={self._arrival_date}, "
            f"dead={self._dead}"
            f")"
        )