import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]

cursor.execute("SELECT AVG(marks) FROM students")
average_marks = cursor.fetchone()[0]

cursor.execute("SELECT MAX(marks) FROM students")
highest_marks = cursor.fetchone()[0]

cursor.execute("SELECT MIN(marks) FROM students")
lowest_marks = cursor.fetchone()[0]

cursor.execute("SELECT SUM(marks) FROM students")
total_marks = cursor.fetchone()[0]

print("Total Students :", total_students)
print("Average Marks  :", average_marks)
print("Highest Marks  :", highest_marks)
print("Lowest Marks   :", lowest_marks)
print("Total Marks    :", total_marks)

connection.close()