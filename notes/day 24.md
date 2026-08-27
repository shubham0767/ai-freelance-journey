Day 24 Notes — Database Transactions
1. What is a database transaction?

A database transaction is a group of database operations treated as one unit.

For example, transferring money involves:

Deducting money from one account.
Adding money to another account.

Both operations should succeed together.

2. What does commit() do?

commit() permanently saves changes made to the database.

connection.commit()

Without commit(), changes such as INSERT, UPDATE, or DELETE may not be saved.

3. What does rollback() do?

rollback() undoes changes made during the current transaction if something goes wrong.

connection.rollback()
4. Why are transactions important?

Transactions help keep the database safe and consistent.

They make sure that related operations are completed properly instead of leaving the database partially updated.

5. What happens if a transaction fails?

If a transaction fails, we can use:

connection.rollback()

to undo the changes made during that transaction.

6. What is database consistency?

Database consistency means that the data remains correct, valid, and follows the rules of the database after an operation.

For example, a bank transfer should not deduct money without adding it to the other account.

7. Why should UPDATE and DELETE usually use WHERE?

WHERE identifies which records should be changed or deleted.

Example:

UPDATE students
SET marks = 90
WHERE student_id = 1;

Without WHERE, the command could update every student.

Similarly:

DELETE FROM students
WHERE student_id = 1;

Without WHERE, all student records could be deleted.

8. Why should we use try-except with database operations?

try-except allows us to handle database errors without crashing the program.

Example:

try:
    cursor.execute(...)
    connection.commit()
except sqlite3.Error:
    connection.rollback()
9. What is the purpose of finally?

finally contains code that should run whether an error occurs or not.

It is commonly used to close the database connection:

finally:
    connection.close()
10. What is the difference between commit() and rollback()?
commit()	rollback()
Saves changes	Undoes changes
Used when operation succeeds	Used when operation fails
Makes changes permanent	Returns to previous state

Easy way to remember:

commit()   → SAVE
rollback() → UNDO
11. Give two real-world examples where transactions are important.

🏦 Banking

When transferring ₹5,000 from one account to another, money should be deducted from one account and added to the other. If something fails, the transaction can be rolled back.

🛒 Online Shopping

When placing an order, the system may need to:

Create the order
Reduce product stock
Record payment

If one important operation fails, the transaction can prevent an incomplete order from being saved.

🧠 Day 24 Quick Revision
Transaction → Group of database operations
commit()    → Save changes
rollback()  → Undo changes
try-except  → Handle errors
finally     → Always execute cleanup
WHERE       → Select specific records
Consistency → Keep data correct and valid