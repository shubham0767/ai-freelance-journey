import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

student_id = int(input("Enter student ID: "))
new_marks = int(input("Enter new marks: "))

cursor.execute("""
UPDATE students
SET marks = ?
WHERE student_id = ?
""", (new_marks, student_id))

connection.commit()

if cursor.rowcount > 0:
    print("Student marks updated successfully.")
else:
    print("Student not found.")

connection.close()