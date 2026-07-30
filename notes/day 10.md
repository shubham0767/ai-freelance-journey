# Day 10 - File Handling in Python

## 1. What is file handling?

File handling is the process of creating, reading, writing, and updating files using Python. It allows programs to store data permanently on a computer.

---

## 2. What are the modes "r", "w", "a", and "x"?

- **r (Read):** Opens a file for reading.
- **w (Write):** Creates a new file or overwrites an existing file.
- **a (Append):** Adds data to the end of an existing file.
- **x (Create):** Creates a new file. It gives an error if the file already exists.

---

## 3. What is the difference between "w" and "a" mode?

| Write (w) | Append (a) |
|------------|------------|
| Deletes old content | Keeps old content |
| Writes from the beginning | Adds data at the end |

---

## 4. What does `with open()` do?

`with open()` opens a file and automatically closes it after the block of code finishes. This helps prevent resource leaks and makes code easier to write.

Example:

```python
with open("student.txt", "r") as file:
    print(file.read())
```

---

## 5. What is the difference between `read()` and `readlines()`?

- **read()** reads the entire file as one string.
- **readlines()** reads the file line by line and returns a list.

Example:

```python
content = file.read()
```

```python
lines = file.readlines()
```

---

## 6. Give two real-life examples where file handling is useful.

### Example 1: Student Management System

Student records can be stored in a file and accessed later.

### Example 2: To-Do List Application

Tasks entered by the user can be saved in a file so they remain available even after the program is closed.

---

# Key Points

- File handling is used to store and retrieve data.
- `"r"` reads a file.
- `"w"` writes and overwrites a file.
- `"a"` appends data to a file.
- `"x"` creates a new file.
- `read()` returns the whole file as a string.
- `readlines()` returns a list of lines.
- `with open()` automatically closes the file.