import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
marks = int(input("Enter marks: "))

cursor.execute("""
INSERT INTO students (name, age, course, marks)
VALUES (?, ?, ?, ?)
""", (name, age, course, marks))

connection.commit()

print("Student added successfully.")

connection.close()