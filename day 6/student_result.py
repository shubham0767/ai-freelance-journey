print("=" * 40)
print("Student Result System")
print("=" * 40)

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return total/5

def calculate_grade(percentage):
    if percentage>=90:
        return "A+"
    elif percentage >=80:
        return"A"
    elif percentage >=70:
        return "B"
    elif percentage >=60:
        return "C"
    elif percentage >=50:
        return "D"
    elif percentage >=35:
        return "E"
    else :
        return "F"

def display_result(name, total, percentage, grade):
    print("\n" + "=" * 40)
    print("STUDENT RESULT")
    print("=" * 40)
    print(f"Name       : {name}")
    print(f"Total      : {total}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")

    if percentage >= 35:
        print("Result     : Pass")
    else:
        print("Result     : Fail")

    print("=" * 40)

name = input("Enter Student Name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)
    
total = calculate_total(marks)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

display_result(name, total, percentage, grade)