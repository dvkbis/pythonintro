from model.animal import Animal

class Dog(Animal):

    PROBA_DEATH = 1
    SOUND = "Woaf!"

    def __init__(self, name, weight, size, gender, age, collar_color, trained, breed):
        super().__init__(name, weight, size, gender, age)
        self.__collar_color = collar_color
        self.__trained = trained
        self.__breed = breed

    ###################
    ## GETTER // SETTER
    ###################
    @property
    def collar_color(self):
        return self.__collar_color
    
    @collar_color.setter
    def collar_color(self, collar_color):
        self.__collar_color = collar_color

    @property
    def trained(self):
        return self.__trained

    @trained.setter
    def trained(self, trained):
        self.__trained = trained

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    ######################
    ## ABSTRACT OVERRIDE
    ######################
    def death_probability(self) -> float:
        return self.PROBA_DEATH

    def make_sound(self) -> str:
        return self.SOUND


    #########################
    ## OTHERS OVERRIDE
    #########################

    def get_description(self) -> str:
        return (
            f"(dog) {super().get_description()}, "
            f" Breed: {self.breed}, "
            f" Trained: {'Oui' if self.trained else 'Non'}, "
            f" Collar: {self.collar_color} "
        )
