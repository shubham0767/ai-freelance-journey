Day 21 Notes — CRUD & SQLite
1. What is CRUD?

CRUD stands for:

C → Create
R → Read
U → Update
D → Delete

These are the four basic operations performed on data in a database.

2. What does Create mean in CRUD?

Create means adding new data to a database.

In SQL, we commonly use INSERT.

Example:

INSERT INTO students (name, marks)
VALUES ('Shubham', 85);
3. What does Read mean?

Read means retrieving or viewing data from a database.

In SQL, we use SELECT.

Example:

SELECT * FROM students;
4. What does Update mean?

Update means changing existing data in a database.

In SQL, we use UPDATE.

Example:

UPDATE students
SET marks = 90
WHERE id = 1;
5. What does Delete mean?

Delete means removing existing data from a database.

In SQL, we use DELETE.

Example:

DELETE FROM students
WHERE id = 1;
6. What is fetchone()?

fetchone() retrieves one record from the results of a query.

Example:

cursor.execute("SELECT * FROM students")


student = cursor.fetchone()


print(student)
7. What is fetchall()?

fetchall() retrieves all records returned by a query.

Example:

cursor.execute("SELECT * FROM students")


students = cursor.fetchall()


for student in students:
    print(student)
8. What is executemany()?

executemany() executes the same SQL statement for multiple sets of values.

Example:

students = [
    ("Shubham", 85),
    ("Rahul", 78),
    ("Amit", 92)
]


cursor.executemany(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    students
)

This is useful when inserting many records at once.

9. Why do we use WHERE in SQL?

WHERE is used to specify which records should be affected by a SQL operation.

Example:

UPDATE students
SET marks = 95
WHERE id = 2;

Only the student with id = 2 will be updated.

Without WHERE, an UPDATE or DELETE can affect all records.

10. Why should we use ? placeholders when inserting user input?

? placeholders allow us to safely pass user-provided values into SQL queries.

Example:

cursor.execute(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    (name, marks)
)

This helps prevent SQL injection and avoids manually building SQL strings with user input.

11. What is rowcount?

rowcount tells us how many rows were affected by the most recent database operation.

Example:

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (student_id,)
)


print(cursor.rowcount)

If one student was deleted:

1

If no matching student was found:

0
12. Give two real-world examples of CRUD systems.
🏦 Banking System

A banking application can use CRUD to:

Create → Create a customer/account
Read → View account information
Update → Update customer details
Delete → Remove or close records
🎓 College Student Management System

A college application can:

Create → Add a student
Read → View student details
Update → Update marks or course
Delete → Remove a student record
🧠 Day 21 Quick Revision
CREATE → INSERT → Add data
READ   → SELECT → View data
UPDATE → UPDATE → Change data
DELETE → DELETE → Remove data

And remember:

fetchone()    → One record
fetchall()    → All records
executemany() → Multiple records
WHERE         → Select specific records
?             → Safe SQL placeholders
rowcount      → Number of affected rows

