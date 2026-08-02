print("=" * 35)
print("Vehicle and Car")
print("=" * 35)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand)
        self.model = model
        self.year = year

    def display(self):
        print("\nCar Details")
        print("=" * 35)
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Year  :", self.year)

car = Car("Toyota", "Fortuner", 2024)

car.display()