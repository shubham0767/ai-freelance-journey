import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Create students table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course_id INTEGER,
    marks INTEGER
)
""")

connection.commit()

try:
    student_id = int(input("Enter student ID: "))
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")

    else:
        cursor.execute("""
        UPDATE students
        SET marks = ?
        WHERE student_id = ?
        """, (marks, student_id))

        if cursor.rowcount > 0:
            connection.commit()
            print("Marks updated successfully.")
        else:
            print("Student not found.")

except ValueError:
    print("Please enter valid numbers.")

except sqlite3.Error as error:
    connection.rollback()
    print("Database error:", error)

finally:
    connection.close()