# Day 05 - Loops in Python

## 1. What is a loop?

A loop is a programming concept that allows a block of code to run repeatedly until a condition is met or for a fixed number of times. It helps reduce repetitive code and makes programs more efficient.

### Example

```python
for i in range(5):
    print("Hello")
```

Output:

```
Hello
Hello
Hello
Hello
Hello
```

---

## 2. What is the difference between `for` and `while`?

### `for` Loop
- Used when the number of iterations is known.
- Commonly used with `range()` or collections like lists and strings.
- Simpler and easier to read for fixed repetitions.

### `while` Loop
- Used when the number of iterations is unknown.
- Continues running as long as the condition is `True`.
- Useful when waiting for user input or a specific condition.

### Example

**For Loop**

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

**While Loop**

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

## 3. What is `range()`?

`range()` is a built-in Python function that generates a sequence of numbers. It is mainly used with `for` loops.

### Syntax

```python
range(start, stop, step)
```

- **start** → Starting number (included)
- **stop** → Ending number (not included)
- **step** → Increment or decrement value (optional)

### Examples

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

```python
for i in range(0, 11, 2):
    print(i)
```

Output:

```
0
2
4
6
8
10
```

---

## 4. When should we use a `for` loop?

Use a `for` loop when you know exactly how many times you want to repeat a task.

### Examples

- Printing numbers from 1 to 20.
- Displaying a multiplication table.
- Reading every item in a list.
- Processing each character in a string.

### Example

```python
for i in range(1, 11):
    print(i)
```

---

## 5. When should we use a `while` loop?

Use a `while` loop when the number of repetitions is not known in advance. The loop continues until the condition becomes `False`.

### Examples

- Login system
- Number guessing game
- Countdown timer
- Menu-driven programs

### Example

```python
password = ""

while password != "python":
    password = input("Enter Password: ")

print("Access Granted!")
```

---

## 6. Give two real-life examples where loops are useful.

### Example 1: ATM PIN Verification

An ATM keeps asking for your PIN until you enter the correct one.

```python
while pin != correct_pin:
    pin = input("Enter PIN: ")
```

---

### Example 2: Student Attendance

A teacher enters attendance for every student in the class.

```python
for student in range(1, 31):
    print("Attendance for Student", student)
```

---

# Key Points

- A loop repeats a block of code.
- Python has two main loops: `for` and `while`.
- `range()` generates a sequence of numbers.
- Use a `for` loop when the number of repetitions is known.
- Use a `while` loop when repetition depends on a condition.
- Loops reduce repetitive code and make programs more efficient.