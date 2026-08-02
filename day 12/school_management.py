print("=" * 40)
print("School Management System")
print("=" * 40)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
        print("\n" + "=" * 30)
        print("STUDENT DETAILS")
        print("=" * 30)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Roll No    :", self.roll_no)
        print("Course     :", self.course)
        print("=" * 30)

name = input("Enter Name: ")
age = int(input("Enter Age: "))
roll_no = input("Enter Roll Number: ")
course = input("Enter Course: ")

student=Student(name,age,roll_no,course)
student.display_details()