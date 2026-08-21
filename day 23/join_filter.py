import sqlite3

connection=sqlite3.connect("college.db")
cursor=connection.cursor()

cursor.execute("""
SELECT students.name, courses.course_name, students.marks
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id
WHERE students.marks > 80
ORDER BY students.marks DESC
""")

students=cursor.fetchall()
for student in students:
    print(student)

connection.close()