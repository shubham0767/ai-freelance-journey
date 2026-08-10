# Day 16 - Lambda Functions, List Comprehensions, map(), filter(), and reduce()

## 1. What is a lambda function?

A lambda function is a small anonymous (unnamed) function that can be written in a single line. It is useful for simple operations.

Example:

```python
square = lambda x: x * x
```

---

## 2. How is a lambda function different from a normal function?

| Normal Function | Lambda Function |
|-----------------|-----------------|
| Uses `def` keyword | Uses `lambda` keyword |
| Can have multiple statements | Contains only one expression |
| Has a function name | Usually anonymous (no name) |

Example:

```python
def add(a, b):
    return a + b
```

```python
add = lambda a, b: a + b
```

---

## 3. What is list comprehension?

List comprehension is a short and efficient way to create a new list using a single line of code.

Example:

```python
numbers = [i for i in range(1, 6)]
```

---

## 4. What does `map()` do?

`map()` applies a function to every item in an iterable and returns a new iterable.

Example:

```python
numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))
```

Output:

```
[2, 4, 6]
```

---

## 5. What does `filter()` do?

`filter()` selects only those elements that satisfy a condition.

Example:

```python
numbers = [1, 2, 3, 4]

even = list(filter(lambda x: x % 2 == 0, numbers))
```

Output:

```
[2, 4]
```

---

## 6. What does `reduce()` do?

`reduce()` repeatedly applies a function to combine all elements into a single value.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, numbers)
```

Output:

```
10
```

---

## 7. Give two real-life examples where lambda functions or list comprehensions are useful.

### Example 1: Student Marks

Use `filter()` to find students who passed and `map()` to add grace marks.

### Example 2: Employee Salaries

Use `map()` to increase salaries by a percentage and `filter()` to display employees earning above a certain amount.

---

# Key Points

- Lambda functions are short anonymous functions.
- List comprehensions create lists in a concise way.
- `map()` transforms every element.
- `filter()` selects elements based on a condition.
- `reduce()` combines elements into one result.
- These features make Python code shorter, cleaner, and more efficient.