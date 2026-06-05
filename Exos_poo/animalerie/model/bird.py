from model.animal import Animal, Gender

class Bird(Animal):
    PROBA_DEATH = 20
    MALE_SOUND = "Pew Pew!"
    FEMALE_SOUND = "Cew Cew!"

    def __init__(self, name, weight, size, gender, age, color, habitat):
        super().__init__(name, weight, size, gender, age)
        self.__color = color
        self.__habitat = habitat

    ## GETTER / SETTER
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def habitat(self):
        return self.__habitat
    
    @habitat.setter
    def habitat(self, habitat):
        self.habitat = self.habitat

    ## ABSTRACT METHOD OVERRIDE
    ###########################
    def death_probability(self) -> float:
        return self.PROBA_DEATH

    def make_sound(self) -> str:
        return self.MALE_SOUND if self.gender == Gender.MALE else self.FEMALE_SOUND
    
    ## OTHER OVERRIDE
    ##############################
    def get_description(self):
        return (
            f"(bird) {super().get_description()}, "
            f"Color: {self.color}, "
            f"Habitat: {self.habitat}"
        )
