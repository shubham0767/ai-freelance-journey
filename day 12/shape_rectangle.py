print("=" * 35)
print("Shape and Rectangle")
print("=" * 35)

class Shape:
    def area(self):
        print("Area cannot be calculated.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area = ",self.length *self.width )

length=float(input("Enter Length :"))
width =  float(input("Enter Width : "))

rect=Rectangle(length,width)

rect.area()