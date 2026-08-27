import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")

connection.commit()

name = input("Enter student name: ")

cursor.execute("""
SELECT * FROM students
WHERE name LIKE ?
""", ("%" + name + "%",))

students = cursor.fetchall()

if len(students) == 0:
    print("Student not found.")
else:
    print("\nStudents found:")
    
    for student in students:
        print(student)

connection.close()