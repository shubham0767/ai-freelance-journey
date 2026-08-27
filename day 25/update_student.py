import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

try:
    student_id = int(input("Enter student ID: "))
    marks = int(input("Enter new marks: "))

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
            print("Student updated successfully.")
        else:
            print("Student not found.")

except ValueError:
    print("Please enter valid numbers.")

except sqlite3.Error as error:
    connection.rollback()
    print("Database error:", error)

finally:
    connection.close()