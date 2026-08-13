import sqlite3

connection=sqlite3.connect("students.db")

cursor=connection.cursor()

name = input("Enter name :")
age=int(input("Enter age :"))
course=input("Enter course :")
marks  =input("Enter marks :")

cursor.execute("""
INSERT INTO students (name, age, course, marks)
VALUES (?, ?, ?, ?)
""", (name, age, course, marks))

connection.commit()

print("Student added successfully.")

connection.close()
