import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

try:
    student_id = int(input("Enter student ID: "))

    cursor.execute("""
    DELETE FROM students
    WHERE student_id = ?
    """, (student_id,))

    if cursor.rowcount > 0:
        connection.commit()
        print("Student deleted successfully.")
    else:
        print("Student not found.")

except ValueError:
    print("Please enter a valid ID.")

except sqlite3.Error as error:
    connection.rollback()
    print("Database error:", error)

finally:
    connection.close()

    