students = {}

def add_student():
    roll = input("Roll Number: ")

    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")
    marks = input("Marks: ")

    students[roll] = {
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    print("Student Added Successfully!")

def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print(students[roll])
    else:
        print("Student Not Found.")

def display_students():
    if len(students) == 0:
        print("No Student Records.")

    else:
        for roll, details in students.items():
            print("\nRoll Number:", roll)
            for key, value in details.items():
                print(key + ":", value)

def delete_student():
    roll = input("Enter Roll Number: ")

    try:
        del students[roll]
        print("Student Deleted.")

    except KeyError:
        print("Student Not Found.")

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        display_students()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")