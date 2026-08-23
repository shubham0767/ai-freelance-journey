import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

student_id = int(input("Enter student ID to delete: "))

cursor.execute("""
DELETE FROM students
WHERE student_id = ?
""", (student_id,))

connection.commit()

if cursor.rowcount > 0:
    print("Student deleted successfully.")
else:
    print("Student not found.")

connection.close()