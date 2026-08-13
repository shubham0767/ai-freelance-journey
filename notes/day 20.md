Day 20 Notes — SQLite & Databases
1. What is a database?

A database is an organized collection of data that allows us to store, manage, and retrieve information easily.

Example: A college database can store student names, ages, courses, and marks.

2. What is SQLite?

SQLite is a lightweight, file-based database system. Python provides the built-in sqlite3 module to work with SQLite databases.

Example:

import sqlite3
3. What is a table?

A table is where data is stored inside a database.

It consists of rows and columns.

Example:

Students
--------------------------------
ID | Name    | Course | Marks
--------------------------------
1  | Shubham | BCA    | 85
2  | Rahul   | BCA    | 78
4. What is a primary key?

A primary key is a column that uniquely identifies each record in a table.

Example:

id INTEGER PRIMARY KEY

Here, each student has a unique id.

5. What does sqlite3.connect() do?

sqlite3.connect() connects Python to an SQLite database.

Example:

connection = sqlite3.connect("students.db")

If the database file doesn't already exist, SQLite can create it.

6. What is a cursor?

A cursor is an object used to execute SQL commands and retrieve data from a database.

Example:

cursor = connection.cursor()
7. What does execute() do?

execute() runs an SQL command.

Example:

cursor.execute("SELECT * FROM students")

It can be used to execute commands such as:

SELECT
INSERT
UPDATE
DELETE
CREATE TABLE
8. Why do we use commit()?

commit() saves changes made to the database.

For example, after inserting a student:

connection.commit()

Without committing, changes may not be permanently saved.

9. What does SELECT do?

SELECT is used to retrieve data from a database.

Example:

SELECT * FROM students;

This retrieves all records from the students table.

10. What do INSERT, UPDATE, and DELETE do?
INSERT

Adds new data.

INSERT INTO students (name, marks)
VALUES ('Shubham', 85);
UPDATE

Changes existing data.

UPDATE students
SET marks = 90
WHERE id = 1;
DELETE

Removes data.

DELETE FROM students
WHERE id = 1;
11. What is the difference between a text file and a database?
Text File	Database
Stores data as plain text	Stores data in structured tables
Difficult to search and update large amounts of data	Easy to search, update, and manage data
Less suitable for complex data	Suitable for large and structured data
Example: students.txt	Example: students.db
12. Give two real-life examples where databases are useful.
🏦 Banking System

Banks use databases to store:

Customer information
Account details
Transactions
Account balances
🎓 College Management System

Colleges use databases to store:

Student details
Marks
Courses
Attendance
Examination records
🧠 Day 20 Quick Revision

Remember these:

Database     → Organized collection of data
SQLite       → Lightweight database system
Table        → Stores data in rows and columns
Primary Key  → Uniquely identifies a record
connect()    → Connects Python to database
cursor       → Executes SQL commands
execute()    → Runs SQL
commit()     → Saves changes
SELECT       → Gets data
INSERT       → Adds data
UPDATE       → Changes data
DELETE       → Removes data