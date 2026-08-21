1. What is a database relationship?

A database relationship is a connection between two or more tables using related columns.

For example:

Students
course_id
   ↓
Courses
course_id

A student can be connected to a particular course.

2. What is a primary key?

A primary key is a column that uniquely identifies each record in a table.

Example:

student_id INTEGER PRIMARY KEY

Each student should have a unique student_id.

3. What is a foreign key?

A foreign key is a column that connects one table to another table.

Example:

FOREIGN KEY (course_id) REFERENCES courses(course_id)

Here, course_id in the students table refers to course_id in the courses table.

4. Why do we use multiple tables?

We use multiple tables to:

Organize data properly
Avoid unnecessary duplicate data
Make databases easier to maintain
Create relationships between different types of data

For example, instead of storing "BCA" repeatedly for every student, we can store courses separately.

5. What is a JOIN?

A JOIN combines data from two or more related tables.

Example:

SELECT students.name, courses.course_name
FROM students
JOIN courses
ON students.course_id = courses.course_id;

This allows us to display the student's name along with their course.

6. What is an INNER JOIN?

An INNER JOIN returns only records that have a matching value in both tables.

Example:

SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id;

If a student doesn't have a matching course, that student won't appear in the result.

7. What is a LEFT JOIN?

A LEFT JOIN returns all records from the left table, even if there is no matching record in the right table.

Example:

SELECT courses.course_name, students.name
FROM courses
LEFT JOIN students
ON courses.course_id = students.course_id;

This can show courses even if no student is enrolled in them.

8. What does ON do in a JOIN?

ON specifies the condition used to connect the tables.

Example:

ON students.course_id = courses.course_id

It tells SQL that the course_id columns are related.

9. What is GROUP BY?

GROUP BY groups records that have the same value.

It is commonly used with functions such as:

COUNT()
SUM()
AVG()
MAX()
MIN()

Example:

SELECT course_id, COUNT(*)
FROM students
GROUP BY course_id;

This counts students in each course.

10. What is HAVING?

HAVING is used to filter grouped results.

Example:

SELECT course_id, COUNT(*)
FROM students
GROUP BY course_id
HAVING COUNT(*) > 2;

This displays only courses having more than 2 students.

11. What is the difference between WHERE and HAVING?
WHERE	HAVING
Filters individual rows	Filters grouped results
Used before GROUP BY	Usually used after GROUP BY
Filters normal records	Filters aggregate results

Example:

-- WHERE
SELECT * FROM students
WHERE marks > 80;
-- HAVING
SELECT course_id, AVG(marks)
FROM students
GROUP BY course_id
HAVING AVG(marks) > 80;

Easy way to remember:

WHERE  → Filter rows
HAVING → Filter groups
12. Give two real-world examples where database relationships are useful.
🛒 Online Shopping

An e-commerce system can have:

Customers
    ↓
Orders
    ↓
Products

A customer can have multiple orders, and each order can contain multiple products.

🎓 College Management

A college system can have:

Students
    ↓
Courses
    ↓
Subjects

Students can be connected to courses and subjects through IDs.

🧠 Day 23 Quick Revision
Primary Key  → Uniquely identifies a record
Foreign Key  → Connects tables
JOIN         → Combines tables
INNER JOIN   → Matching records only
LEFT JOIN    → All left-table records
ON           → JOIN condition
GROUP BY     → Creates groups
HAVING       → Filters groups
WHERE        → Filters rows