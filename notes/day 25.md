Day 25 Notes — CRUD Applications
1. What is CRUD?

CRUD stands for:

C — Create
R — Read
U — Update
D — Delete

These are the four basic operations performed on data in a database.

2. How does a CRUD application work?

A CRUD application allows users to:

Create → Add new data
Read   → View existing data
Update → Modify data
Delete → Remove data

For example, a Student Management System can add, view, update, and delete student records.

3. What is a menu-driven program?

A menu-driven program displays different options to the user and performs an action based on their choice.

Example:

1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
4. Why do we use functions in a large program?

Functions divide a large program into smaller, organized parts.

For example:

add_student()
view_students()
update_student()
delete_student()

This makes the program easier to:

Read
Test
Debug
Maintain
Reuse
5. Why should database connections be closed?

Database connections should be closed after use to:

Release system resources
Prevent unnecessary open connections
Keep the database system efficient
Avoid potential database problems

Example:

connection.close()
6. Why should SQL queries use ? placeholders?

? placeholders safely insert user-provided values into SQL queries.

Example:

cursor.execute(
    "SELECT * FROM students WHERE name = ?",
    (name,)
)

They help prevent SQL injection and make queries safer.

7. What is the purpose of commit()?

commit() permanently saves changes made to the database.

Example:

connection.commit()

It is commonly used after:

INSERT
UPDATE
DELETE
8. What is the purpose of rollback()?

rollback() undoes changes made during the current transaction when something goes wrong.

Example:

try:
    # database operation
    connection.commit()

except:
    connection.rollback()
9. Why is exception handling important in a database application?

Exception handling prevents the program from crashing when an error occurs.

For example, it can handle:

Invalid user input
Database errors
Missing tables
Duplicate records
Connection problems
10. What is the purpose of ORDER BY and LIMIT?

ORDER BY is used to sort records.

Example:

SELECT * FROM students
ORDER BY marks DESC;

LIMIT restricts how many records are returned.

Example:

SELECT * FROM students
ORDER BY marks DESC
LIMIT 3;

This gives the top 3 students.

11. What is the difference between fetchone() and fetchall()?
fetchone()	fetchall()
Returns one record	Returns all remaining records
Useful when one result is needed	Useful when multiple results are needed

Example:

student = cursor.fetchone()

returns one record.

students = cursor.fetchall()

returns multiple records.

12. Give two examples of real-world CRUD applications.

🎓 Student Management System

Create → Add student
Read → View student
Update → Change marks
Delete → Remove student

🛒 E-commerce System

Create → Add a product/order
Read → View products/orders
Update → Change product details
Delete → Remove a product/order
🧠 Day 25 Quick Revision
CRUD       → Create, Read, Update, Delete
Functions  → Organize code
Menu       → User chooses an operation
?          → Safe SQL parameters
commit()   → Save changes
rollback() → Undo changes
ORDER BY   → Sort records
LIMIT      → Limit results
fetchone() → Get one record
fetchall() → Get all records