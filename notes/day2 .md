# Day 2 Notes

## 1. What is a variable?

A variable is a named storage location used to store data in a program. The value of a variable can change while the program is running.

**Example:**
```python
name = "Shubham"
age = 21
```

---

## 2. What are the four basic data types?

The four basic data types in Python are:

- **str (String)** → Stores text.
  ```python
  name = "Shubham"
  ```

- **int (Integer)** → Stores whole numbers.
  ```python
  age = 21
  ```

- **float** → Stores decimal numbers.
  ```python
  height = 5.8
  ```

- **bool (Boolean)** → Stores `True` or `False`.
  ```python
  student = True
  ```

---

## 3. What is type conversion?

Type conversion is the process of changing one data type into another.

**Example:**
```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

---

## 4. Why do we use `input()`?

The `input()` function is used to take input from the user while the program is running.

**Example:**
```python
name = input("Enter your name: ")
```

---

## 5. What are f-strings?

f-strings are used to insert variables directly into a string. They make the code easier to read and write.

**Example:**
```python
name = "Shubham"
print(f"My name is {name}")
```

**Output:**
```
My name is Shubham
```