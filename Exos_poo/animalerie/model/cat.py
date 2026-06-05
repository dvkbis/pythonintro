from random import randint
from model.animal import Animal, Gender

class Cat(Animal):

    PROBA_DEATH = 30
    SOUND = "Meow!"
    CLAW_MIN = 0
    CLAW_MAX = 6
    CHEAT_LIVES = 4

    def __init__(
        self,
        name: str,
        weight: float,
        size: float,
        gender: Gender,
        age: int,
        personality: str,
        long_hair: bool
    ):
        super().__init__(name, weight, size, gender, age)

        self._personality = personality
        self._long_hair = long_hair
        self._claw_size = randint(self.CLAW_MIN, self.CLAW_MAX - 2)
        self._remaining_lives = self.CHEAT_LIVES

    # Getters / Setters

    @property
    def personality(self):
        return self._personality

    @personality.setter
    def personality(self, value):
        self._personality = value

    @property
    def long_hair(self):
        return self._long_hair

    @long_hair.setter
    def long_hair(self, value):
        self._long_hair = value

    @property
    def claw_cut(self) -> bool:
        return self._claw_size < self.CLAW_MAX

    # Abstract overrides

    def death_probability(self) -> float:
        return self.PROBA_DEATH

    def make_sound(self) -> str:
        return self.SOUND

    # Description override

    def get_description(self) -> str:
        return (
            f"(cat) {super().get_description()}, "
            f"Personality: {self.personality}, "
            f"Hair: {'long' if self.long_hair else 'short'}"
        )

    # Behavior methods

    def pass_day(self):
        super().pass_day()
        self._grow_claws()

    def cut_claws(self):
        self._claw_size = self.CLAW_MIN

    def _grow_claws(self):
        self._claw_size += 1

    def die(self):
        if self._remaining_lives < 0:
            super().die()

        print(f" > {self.name} Dead...?")
        self._remaining_lives -= 1