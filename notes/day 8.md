# Day 08 - Tuples and Dictionaries in Python

## 1. What is a tuple?

A tuple is a collection of multiple values stored in a single variable. It is ordered but **cannot be changed** after it is created. This makes tuples **immutable**.

### Example

```python
colors = ("Red", "Blue", "Green")

print(colors)
```

**Output:**

```
('Red', 'Blue', 'Green')
```

---

## 2. What is the difference between a list and a tuple?

| List | Tuple |
|------|-------|
| Created using square brackets `[]` | Created using parentheses `()` |
| Can be changed (Mutable) | Cannot be changed (Immutable) |
| Items can be added or removed | Items cannot be added or removed after creation |
| Example: `["Apple", "Banana"]` | Example: `("Apple", "Banana")` |

### Example

```python
# List
fruits = ["Apple", "Banana"]
fruits.append("Mango")

# Tuple
colors = ("Red", "Blue", "Green")
```

---

## 3. What is a dictionary?

A dictionary is a collection of data stored as **key-value pairs**. Each key is unique and is used to access its corresponding value.

### Example

```python
student = {
    "name": "Shubham",
    "age": 21,
    "course": "BCA"
}

print(student)
```

**Output:**

```
{'name': 'Shubham', 'age': 21, 'course': 'BCA'}
```

---

## 4. What is a key-value pair?

A key-value pair consists of:

- **Key** → A unique name used to identify the data.
- **Value** → The actual information stored.

### Example

```python
student = {
    "name": "Shubham",
    "age": 21
}
```

Here:

- **Key:** `"name"` → **Value:** `"Shubham"`
- **Key:** `"age"` → **Value:** `21`

---

## 5. How do you access values in a dictionary?

You access a value by using its key inside square brackets.

### Example

```python
student = {
    "name": "Shubham",
    "age": 21,
    "course": "BCA"
}

print(student["name"])
print(student["age"])
print(student["course"])
```

**Output:**

```
Shubham
21
BCA
```

---

## 6. Give two real-life examples where dictionaries are useful.

### Example 1: Student Information

A school system stores student details using keys and values.

```python
student = {
    "Name": "Shubham",
    "Age": 21,
    "Course": "BCA"
}
```

---

### Example 2: Employee Database

A company stores employee details in a dictionary.

```python
employee = {
    "ID": "EMP101",
    "Name": "Rahul",
    "Department": "IT",
    "Salary": 50000
}
```

---

# Key Points

- A tuple stores multiple values and cannot be changed after creation.
- Lists are mutable, while tuples are immutable.
- A dictionary stores data as key-value pairs.
- Keys are unique and are used to access values.
- Dictionary values are accessed using `dictionary[key]`.
- Dictionaries are widely used in Python, APIs, databases, and AI applications.