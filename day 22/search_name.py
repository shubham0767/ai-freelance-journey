import sqlite3
connection=sqlite3.connect("students.db")
cursor=connection.cursor()

name=input("Enter name to search:")

cursor.execute("""
SELECT * FROM students
WHERE name LIKE?
""",("%"+name+"%",))


students=cursor.fetchall()
if students:
    for student in students:
        print(student)
else:
    print("No student found.")

connection.close()