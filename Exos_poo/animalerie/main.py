from model.animal import Animal, Gender
from model.bird import Bird
from model.cat import Cat
from model.dog import Dog
from model.animal_shelter import AnimalShelter

def main():
    animal_shelter = AnimalShelter("PyAnimals")

    animal_shelter.add_animal(
        Cat(
            name="The cat",
            weight=5,
            size=0.5,
            gender=Gender.FEMALE,
            age=4,
            personality="Playful",
            long_hair=False
        )
    )

    animal_shelter.add_animal(
        Dog(
            name="The dog",
            weight=12,
            size=0.3,
            gender=Gender.MALE,
            age=15,
            collar_color="Blue",
            trained=False,
            breed="Basset"
        )
    )

    animal_shelter.add_animal(
        Cat(
            name="Bernard",
            weight=6,
            size=0.5,
            gender=Gender.MALE,
            age=12,
            personality="Cuddly",
            long_hair=True
        )
    )

    animal_shelter.add_animal(
        Bird(
            name="Tweety",
            weight=0.1,
            size=0.01,
            gender=Gender.FEMALE,
            age=9,
            color="Yellow",
            habitat="Cage"
        )
    )

    animal_shelter.add_animal(
        Cat(
            name="Sylvester",
            weight=15,
            size=0.7,
            gender=Gender.MALE,
            age=10,
            personality="Hunter",
            long_hair=False
        )
    )

    animal_shelter.add_animal(
        Dog(
            name="Rex",
            weight=15,
            size=0.7,
            gender=Gender.MALE,
            age=5,
            collar_color="Red",
            trained=True,
            breed="German Shepherd"
        )
    )

    # Simulation loop
    while animal_shelter.animals:

        print(animal_shelter.get_animals_description())

        info = animal_shelter.simulate_day()

        print(info)
        print()

        input("Press Enter to continue...")
if __name__ == "__main__":
    main()