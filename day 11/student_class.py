print("=" * 35)
print("Student Class")
print("=" * 35)


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student1=Student("Shubham",21)
print("Name :",student1.name)
print("Age  : ", student1.age)