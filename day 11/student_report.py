print("=" * 40)
print("Student Report Card")
print("=" * 40)

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 35:
            return "D"
        else:
            return "Fail"

    def display_report(self):
        print("\n" + "=" * 30)
        print("STUDENT REPORT CARD")
        print("=" * 30)
        print("Name       :", self.name)
        print("Roll No    :", self.roll)
        print("Total      :", self.calculate_total())
        print("Percentage :", self.calculate_percentage())
        print("Grade      :", self.calculate_grade())
        print("=" * 30)

name = input("Enter Name: ")
roll = input("Enter Roll Number: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter Marks of Subject {i+1}: "))
    marks.append(mark)

student = Student(name, roll, marks)

student.display_report()