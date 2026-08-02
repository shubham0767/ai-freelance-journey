print("=" * 35)
print("Person and Student")
print("=" * 35)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,college):
        super().__init__(name, age)
        self.college=college

    def display(self):
        print("\n Student Details")
        print("="*35)
        print("Name   :",self.name)
        print("Age     :",self.age)
        print("College :",self.college)

student=Student("Shubham",21,"Shailendra Education Society")

student.display()