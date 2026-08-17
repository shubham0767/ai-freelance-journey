import sqlite3

connection=sqlite3.connect("students.db")
cursor=connection.cursor()

cursor.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 3
""")

students=cursor.fetchall()
for student in students:
    print(student)

connection.close()