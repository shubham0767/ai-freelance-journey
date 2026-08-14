import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

name = input("Enter student name: ")

cursor.execute(
    "SELECT * FROM students WHERE name = ?",
    (name,)
)

student = cursor.fetchone()

if student:
    print("Student Found")
    print("ID      :", student[0])
    print("Name    :", student[1])
    print("Age     :", student[2])
    print("Course  :", student[3])
    print("Marks   :", student[4])
else:
    print("Student not found.")

connection.close()