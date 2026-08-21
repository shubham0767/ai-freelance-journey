import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("""
SELECT courses.course_name, COUNT(students.student_id)
FROM courses
LEFT JOIN students
ON courses.course_id = students.course_id
GROUP BY courses.course_name
""")

results = cursor.fetchall()

for result in results:
    print(result)

connection.close()