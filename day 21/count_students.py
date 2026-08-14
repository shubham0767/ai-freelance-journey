import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM students")

count = cursor.fetchone()[0]

print("Total Students:", count)

connection.close()