# Day 11 - Object-Oriented Programming (OOP)

## 1. What is a class?

A class is a blueprint or template used to create objects. It defines the attributes (data) and methods (functions) that objects will have.

Example:

```python
class Student:
    pass
```

---

## 2. What is an object?

An object is an instance of a class. It is created using a class and contains its own data.

Example:

```python
student1 = Student()
```

---

## 3. What is the purpose of `__init__()`?

`__init__()` is a special constructor method. It runs automatically when an object is created and is used to initialize the object's attributes.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

## 4. What does `self` represent?

`self` refers to the current object. It is used to access the object's attributes and methods inside the class.

Example:

```python
self.name = name
```

---

## 5. What is the difference between a class and an object?

| Class | Object |
|-------|--------|
| Blueprint or template | Instance created from the class |
| Defines properties and methods | Stores actual values |
| Created using `class` | Created by calling the class |

---

## 6. Give two real-life examples of classes and objects.

### Example 1: Car

**Class:** Car

**Objects:**

- Toyota Fortuner
- Honda City
- Hyundai Creta

---

### Example 2: Student

**Class:** Student

**Objects:**

- Shubham
- Rahul
- Priya

---

# Key Points

- A class is a blueprint.
- An object is an instance of a class.
- `__init__()` initializes object data.
- `self` refers to the current object.
- Classes contain attributes and methods.
- OOP helps organize code into reusable and structured components.