print("=" * 35)
print("Rectangle Class")
print("=" * 35)

class Rectangle:
    def __init__(self,lenght,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length* self.width

    def perimeter(self):
        return 2*(self.length + self.width)

length=float(input("Enter Length :"))
width = float(input("Enter Width :"))

rect = Rectangle(length,width)

print("\n Area =",rect.area())
print("Perimeter =",rect.perimeter())