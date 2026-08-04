# Day 13 - Exception Handling in Python

## 1. What is an exception?

An exception is an error that occurs while a program is running. If not handled, it can stop the program.

Example:

```python
print(10 / 0)
```

This raises a `ZeroDivisionError`.

---

## 2. Why do we use `try` and `except`?

`try` is used to write code that may cause an error.

`except` is used to handle the error so the program does not crash.

Example:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
```

---

## 3. What is the purpose of the `else` block?

The `else` block runs only if no exception occurs in the `try` block.

Example:

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)
```

---

## 4. What is the purpose of the `finally` block?

The `finally` block always executes, whether an exception occurs or not. It is often used to close files or release resources.

Example:

```python
try:
    file = open("data.txt", "r")
finally:
    file.close()
```

---

## 5. Name three common exceptions in Python.

- ValueError
- ZeroDivisionError
- FileNotFoundError

---

## 6. Give two real-life examples where exception handling is useful.

### Example 1: ATM System

If the user enters invalid input or tries to withdraw more money than available, the program can display an error message instead of crashing.

### Example 2: File Reader

If the requested file does not exist, the program can show "File not found" instead of stopping unexpectedly.

---

# Key Points

- Exceptions are runtime errors.
- `try` contains code that might raise an exception.
- `except` handles specific errors.
- `else` runs only when no exception occurs.
- `finally` always runs.
- Exception handling makes programs more reliable and user-friendly.