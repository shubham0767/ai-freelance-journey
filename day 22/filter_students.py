import sqlite3

connection=sqlite3.connect("students.db")
cursor=connection.cursor()

marks=int(input("Enter minimum marks :"))

cursor.execute("""
SELECT * FROM students
WHERE marks>=?
""",(marks,))

students=cursor.fetchall()
for student in students:
    print(student)

connection.close()