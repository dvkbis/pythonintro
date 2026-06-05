from model.animal import Animal, Gender
from model.bird import Bird
from model.cat import Cat
from model.dog import Dog
from model.animal_shelter import AnimalShelter

def main():
    animal_shelter = AnimalShelter("PyAnimals")

    animal_shelter.add_animal(
        Cat(
            name="Garfield",
            weight=7,
            size=0.5,
            gender=Gender.MALE,
            age=4,
            personality="Playful",
            long_hair=False
        )
    )

    animal_shelter.add_animal(
        Dog(
            name="Lassie",
            weight=12,
            size=0.3,
            gender=Gender.FEMALE,
            age=15,
            collar_color="Blue",
            trained=False,
            breed="Colley"
        )
    )

    animal_shelter.add_animal(
        Cat(
            name="Puss in boots",
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
        Bird(
            name="Lugia",
            weight=216,
            size=5.2,
            gender=Gender.MALE,
            age=9,
            color="White",
            habitat="Unkown"
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
    day_number = 0

    # Simulation loop
    while animal_shelter.animals:
        day_number += 1
        print("-----------------------")
        print(f"   DAY {day_number}")
        print("-----------------------")

        print(animal_shelter.get_animals_description())

        info = animal_shelter.simulate_day()
        print()
        print("Day is passing...")
        print(f" > {'\n > '.join(info)}")
        print()

        print("Night is passing...")
        info = animal_shelter.simulate_night()
        print(f" > {'\n > '.join(info)}")

        print(
            f"{animal_shelter.name} has "
            f"{animal_shelter.count_birds()} bird(s), "
            f"{animal_shelter.count_cats()} cat(s), "
            f"{animal_shelter.count_dogs()} dog(s)"
            )

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()