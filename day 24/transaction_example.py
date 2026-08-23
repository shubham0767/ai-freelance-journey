import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

try:
    cursor.execute("""
    UPDATE students
    SET marks = marks + 5
    WHERE course_id = 1
    """)

    cursor.execute("""
    UPDATE students
    SET marks = marks - 2
    WHERE course_id = 2
    """)

    connection.commit()

    print("Transaction completed successfully.")

except Exception as e:
    connection.rollback()
    print("Transaction failed.")
    print("Error:", e)

finally:
    connection.close()
    