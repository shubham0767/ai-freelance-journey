print("=" * 35)
print("Animal and Dog")
print("=" * 35)

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass


dog=Dog()
dog.sound()