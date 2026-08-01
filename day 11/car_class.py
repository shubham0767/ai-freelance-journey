print("=" * 35)
print("Car Class")
print("=" * 35)

class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

car1=Car("Toyota","Fortuner",2014)

print("Brand :",car1.brand)
print("Model : ",car1.model)
print("Year  :",car1.year)