1. What is ORDER BY?

ORDER BY is used to sort database records based on a column.

Example:

SELECT * FROM students
ORDER BY marks;
2. What is the difference between ASC and DESC?
ASC → Ascending order, from smallest to largest.
DESC → Descending order, from largest to smallest.

Example:

ORDER BY marks ASC
ORDER BY marks DESC
3. What does WHERE do?

WHERE is used to filter records based on a condition.

Example:

SELECT * FROM students
WHERE marks >= 80;

This displays students who scored 80 or more.

4. What is LIKE used for?

LIKE is used to search for a specific pattern in text.

Example:

SELECT * FROM students
WHERE name LIKE 'Shub%';

This can find names starting with Shub.

5. What does % mean when used with LIKE?

% represents zero or more characters.

Example:

WHERE name LIKE '%am%'

This can find names containing am.

6. What does COUNT() do?

COUNT() counts the number of records.

Example:

SELECT COUNT(*) FROM students;

It returns the total number of students.

7. What does AVG() do?

AVG() calculates the average value of a column.

Example:

SELECT AVG(marks) FROM students;

It calculates the average marks.

8. What do MAX() and MIN() do?
MAX() → Finds the highest value.
MIN() → Finds the lowest value.

Example:

SELECT MAX(marks) FROM students;
SELECT MIN(marks) FROM students;
9. What does SUM() do?

SUM() calculates the total of numeric values.

Example:

SELECT SUM(marks) FROM students;

It calculates the total marks.

10. What is LIMIT?

LIMIT restricts the number of records returned by a query.

Example:

SELECT * FROM students
ORDER BY marks DESC
LIMIT 3;

This displays only the top 3 students.

11. What is the difference between AND and OR?

AND means all conditions must be true.

SELECT * FROM students
WHERE marks >= 80 AND age >= 20;

Both conditions must be satisfied.

OR means at least one condition must be true.

SELECT * FROM students
WHERE marks >= 90 OR age >= 22;

Either condition can be satisfied.

12. Give two real-world examples where filtering and sorting data are useful.

🛒 Online Shopping

Filter products by price or category.
Sort products from lowest to highest price.
Sort products by customer rating.

🎓 College Management System

Filter students who scored above 75.
Sort students according to their marks.
Find the highest and lowest marks.
🧠 Day 22 Quick Revision
ORDER BY → Sort data
ASC       → Small → Large
DESC      → Large → Small
WHERE     → Filter data
LIKE      → Search patterns
%         → Any number of characters
COUNT()   → Count records
AVG()     → Average
MAX()     → Highest
MIN()     → Lowest
SUM()     → Total
LIMIT     → Restrict results
AND       → All conditions
OR        → At least one condition