# Day 12 - Inheritance in Python

## 1. What is inheritance?

Inheritance is a feature of Object-Oriented Programming (OOP) that allows one class to use the attributes and methods of another class. This helps reuse code and reduces duplication.

Example:

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

---

## 2. What is a parent class?

A parent class (also called a base class) is the class whose attributes and methods are inherited by another class.

Example:

```python
class Animal:
    pass
```

---

## 3. What is a child class?

A child class (also called a derived class) inherits from a parent class and can also have its own additional attributes and methods.

Example:

```python
class Dog(Animal):
    pass
```

---

## 4. What does `super()` do?

`super()` is used to call the parent class constructor or methods. It allows the child class to reuse the parent class code.

Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
```

---

## 5. What is method overriding?

Method overriding occurs when a child class provides its own version of a method that already exists in the parent class.

Example:

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```

---

## 6. Give two real-life examples of inheritance.

### Example 1: Vehicle

- Parent Class: Vehicle
- Child Classes: Car, Bike, Bus

---

### Example 2: Person

- Parent Class: Person
- Child Classes: Student, Teacher, Employee

---

# Key Points

- Inheritance allows code reuse.
- The parent class contains common features.
- The child class inherits from the parent class.
- `super()` calls the parent class constructor or methods.
- Method overriding lets a child class replace a parent class method with its own implementation.