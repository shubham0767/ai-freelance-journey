import sqlite3

connection=sqlite3.connect("college.db")
cursor=connection.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS courses(
course_id INTEGER PRIMARY KEY ,
course_name TEXT)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
student_id INTEGER PRIMARY KEY,
name TEXT ,
age INTEGER,
course_id INTEGER,
marks INTEGER,
FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")
connection.commit()

print("Tables Created Successfully.")
connection.close()