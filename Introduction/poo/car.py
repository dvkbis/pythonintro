# Example of object-oriented programming (OOP) in Python
# This file shows how to define classes, create objects, use inheritance,
# and override methods.

class Car:
    """Simple Car class demonstrating Python OOP."""

    def __init__(self, make, model, year, color="white"):
        # Instance attributes
        self.make = make
        self.__model = model
        self.year = year
        self.color = color
        self.speed = 0
    @property
    def model(self):
        self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value

    def description(self):
        """Return a short description of the car."""
        return f"{self.year} {self.make} {self.model} in {self.color}"

    def start(self):
        """Start the car."""
        return f"{self.description()} is starting."

    def accelerate(self, amount=10):
        """Increase the car's speed."""
        self.speed += amount
        return f"Accelerating by {amount} km/h. Current speed: {self.speed} km/h."

    def brake(self, amount=10):
        """Decrease the car's speed without going below zero."""
        self.speed = max(0, self.speed - amount)
        return f"Braking by {amount} km/h. Current speed: {self.speed} km/h."


class ElectricCar(Car):
    """An electric car that inherits from Car and adds battery behavior."""

    def __init__(self, make, model, year, battery_capacity, color="blue"):
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity
        self.charge_level = 100

    def charge(self, amount=10):
        """Charge the electric car battery."""
        self.charge_level = min(100, self.charge_level + amount)
        return f"Charging battery by {amount}%. Charge level: {self.charge_level}% "

    def start(self):
        """Override the base start method with electric-specific behavior."""
        return f"{self.description()} is starting silently with {self.charge_level}% battery."


def main():
    # Create a normal car object
    car = Car("Toyota", "Corolla", 2022, color="red")
    print(car.start())
    print(car.accelerate(30))
    print(car.brake(15))
    print()
    car.__model = "Yaris"
    print(car.__model)

    # Create an electric car object using inheritance
    electric = ElectricCar("Tesla", "Model 3", 2024, battery_capacity=75, color="black")
    print(electric.start())
    print(electric.accelerate(50))
    print(electric.charge(20))
    print(electric.brake(20))
    print()

    # Polymorphism: both objects share the same interface for start()
    for vehicle in (car, electric):
        print(vehicle.start())


if __name__ == "__main__":
    main()
