class Car:
    def __init__(self, make, model, year):
        """Initialize the attributes of the car."""
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        """Print a description of the car in 'Year Make Model' format."""
        print(f"{self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

my_car = Car("Toyota", "Corolla", 2020)
my_car.describe_car()  # Output: 2020 Toyota Corolla