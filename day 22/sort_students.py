import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create students table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")

connection.commit()

# Check if table has students
cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:
    print("No students found in the database.")
else:
    cursor.execute("""
    SELECT * FROM students
    ORDER BY marks DESC
    """)

    students = cursor.fetchall()

    print("\nStudents sorted by marks:")
    print("-" * 40)

    for student in students:
        print(student)

connection.close()