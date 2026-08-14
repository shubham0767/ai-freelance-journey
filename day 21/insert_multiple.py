import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")

students = [
    ("Shubham", 21, "BCA", 85),
    ("Rahul", 20, "BCA", 78),
    ("Amit", 22, "BCA", 92)
]

cursor.executemany("""
INSERT INTO students (name, age, course, marks)
VALUES (?, ?, ?, ?)
""", students)

connection.commit()

print("Students added successfully.")

connection.close()