from model.animal import Animal
from model.dog import Dog
from model.bird import Bird
from model.cat import Cat

class AnimalShelter():

    def __init__(self, name):
        self.__name = name
        self.__animals: list[Animal] = []

    ## GETTER / SETTER
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def animals(self):
        return self.__animals

    ## ANIMAL MANAGEMENT
    def add_animal(self, animal):
        if animal.is_dead:
            raise Exception("You can't add a dead animal")
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def get_animals_description(self):
        desc = "\n > ".join(animal.get_description() for animal in self.animals)

        return f"Animals description: \n > {desc}"
    
    def count_dogs(self) -> int:
        return sum(isinstance(animal, Dog) for animal in self.animals)
    
    def count_birds(self) -> int:
        return sum(isinstance(animal, Bird) for animal in self.animals)
    
    def count_cats(self) -> int:
        return sum(isinstance(animal, Cat) for animal in self.animals)
    
    def simulate_day(self) -> str:
        days_events = []
        for animal in self.animals:
            animal.pass_day()
            ## cat events
            if isinstance(animal, Cat) and animal._claw_size == Cat.CLAW_MAX:
                days_events.append(f"{animal.name}: scratched me !!")
                animal.cut_claws()
                days_events.append(f"{animal.name}: I cut its claws")
                
            days_events.append(f"{animal.name}: {animal.make_sound()}")

        return days_events

    

    def simulate_night(self) -> str:
        night_events = []
        dead_animals = []
        for animal in self.animals:
            animal.pass_night()

            if animal.is_dead:
                night_events.append(f"{animal.name} is dead :(")
                dead_animals.append(animal)

        # Remove all dead animals
        for animal in dead_animals:
            try:
                self.remove_animal(animal)
            except Exception:
                print(f"ERROR : Can't remove this animal : {animal.name}")
        return night_events