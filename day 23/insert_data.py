import sqlite3
connection = sqlite3.connect("college.db")
cursor=connection.cursor()

courses=[
    (1,"BCA"),
    (2,"BBI"),
    (3,"BBA")
]

cursor.executemany("""
INSERT OR IGNORE INTO courses (course_id, course_name)
VALUES(?,?)

""",courses)

students=[
    (1, "Shubham", 21, 1, 85),
    (2, "Rahul", 20, 1, 78),
    (3, "Amit", 22, 2, 92),
    (4, "Priya", 21, 3, 95)
]

cursor.executemany("""
INSERT OR IGNORE INTO students
(student_id,name,age,course_id,marks)
VALUES(?,?,?,?,?)
""",students)

connection.commit()
print("DATA inserted Successfully.")

connection.close()