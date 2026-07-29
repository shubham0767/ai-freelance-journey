# Day 07 - Lists in Python

## 1. What is a list?

A list is a collection of multiple values stored in a single variable. Lists can contain numbers, strings, or different types of data. They are ordered, changeable (mutable), and allow duplicate values.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

**Output:**

```
['Apple', 'Banana', 'Mango']
```

---

## 2. How do you create a list?

A list is created using square brackets `[]`, with items separated by commas.

### Example

```python
students = ["Rahul", "Shubham", "Priya", "Sneha", "Rohit"]
```

You can also create an empty list:

```python
shopping = []
```

Then add items using:

```python
shopping.append("Milk")
shopping.append("Bread")
```

---

## 3. How do you access list elements?

Each item in a list has an index. Indexing starts from **0**.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

**Output:**

```
Apple
Banana
Mango
```

You can also access items from the end using negative indexing.

```python
print(fruits[-1])
```

**Output:**

```
Mango
```

---

## 4. What is the difference between `append()` and `remove()`?

### `append()`

- Adds a new item to the end of a list.

Example:

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

**Output:**

```
['Apple', 'Banana', 'Mango']
```

### `remove()`

- Removes a specific item from the list.

Example:

```python
fruits.remove("Banana")

print(fruits)
```

**Output:**

```
['Apple', 'Mango']
```

### Difference

| append() | remove() |
|-----------|-----------|
| Adds an item | Removes an item |
| Item is added at the end | Removes the first matching item |

---

## 5. What do `len()`, `max()`, `min()`, and `sum()` do?

### `len()`

Returns the total number of items in a list.

```python
numbers = [10, 20, 30]

print(len(numbers))
```

**Output:**

```
3
```

---

### `max()`

Returns the largest value.

```python
numbers = [10, 25, 8, 40]

print(max(numbers))
```

**Output:**

```
40
```

---

### `min()`

Returns the smallest value.

```python
numbers = [10, 25, 8, 40]

print(min(numbers))
```

**Output:**

```
8
```

---

### `sum()`

Returns the total of all numbers in the list.

```python
numbers = [10, 20, 30, 40]

print(sum(numbers))
```

**Output:**

```
100
```

---

## 6. Give two real-life examples where lists are useful.

### Example 1: Shopping List

A shopping app stores multiple items such as:

- Milk
- Bread
- Eggs
- Rice
- Sugar

These items can be stored in a list.

```python
shopping = ["Milk", "Bread", "Eggs", "Rice", "Sugar"]
```

---

### Example 2: Student Marks

A school system stores marks of different subjects in a list.

```python
marks = [80, 75, 90, 65, 85]
```

Using the list, we can calculate:

- Highest marks
- Lowest marks
- Total marks
- Average marks

---

# Key Points

- A list stores multiple values in one variable.
- Lists are created using square brackets `[]`.
- List indexing starts from `0`.
- `append()` adds an item to a list.
- `remove()` deletes an item from a list.
- `len()` counts items.
- `max()` finds the largest value.
- `min()` finds the smallest value.
- `sum()` adds all numeric values in a list.
- Lists are widely used in Python, AI, data analysis, and web development.