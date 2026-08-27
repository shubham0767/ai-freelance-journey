import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

if len(students) == 0:
    print("No students found.")
else:
    for student in students:
        print(student)

connection.close()