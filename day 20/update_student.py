import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

student_id = int(input("Enter student ID: "))
new_marks = int(input("Enter new marks: "))

cursor.execute("""
UPDATE students
SET marks = ?
WHERE id = ?
""", (new_marks, student_id))

connection.commit()

print("Student marks updated.")

connection.close()