# Day 04 - Conditional Statements

## 1. What is an if statement?

An `if` statement is used to make decisions in a program. It checks whether a condition is `True` or `False`. If the condition is `True`, the code inside the `if` block is executed.

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

---

## 2. What is the difference between if, elif, and else?

### if
- Used to check the first condition.
- If the condition is `True`, its block of code runs.

### elif
- Stands for **else if**.
- Used to check another condition if the previous `if` (or `elif`) condition was `False`.
- You can use multiple `elif` statements.

### else
- Runs when none of the previous conditions are `True`.
- It does not require a condition.

### Example

```python
marks = 82

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

else:
    print("Grade B")
```

---

## 3. What are comparison operators?

Comparison operators are used to compare two values. They always return either `True` or `False`.

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

### Example

```python
a = 10
b = 20

print(a < b)
```

Output:

```
True
```

---

## 4. What are logical operators?

Logical operators are used to combine two or more conditions.

### Types

- `and` → Returns `True` if both conditions are `True`.
- `or` → Returns `True` if at least one condition is `True`.
- `not` → Reverses the result (`True` becomes `False` and `False` becomes `True`).

### Example

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

---

## 5. Explain the leap year logic in your own words.

A year is a leap year if it is divisible by **400**, or if it is divisible by **4** but **not divisible by 100**.

Examples:
- 2024 → Leap Year
- 2023 → Not a Leap Year
- 2000 → Leap Year
- 1900 → Not a Leap Year

Python logic:

```python
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

## 6. Give one real-life example of using if-elif-else.

### ATM Withdrawal

```python
balance = 5000
withdraw = 3000

if withdraw > balance:
    print("Insufficient Balance")

elif withdraw <= balance:
    print("Transaction Successful")

else:
    print("Invalid Amount")
```

### Another Example

A student grading system:

- If marks are 90 or above → Grade A+
- Else if marks are 80–89 → Grade A
- Else if marks are 70–79 → Grade B
- Else → Grade C or Fail

This is a practical use of `if`, `elif`, and `else` in everyday applications.

---

## Key Points

- `if` checks the first condition.
- `elif` checks additional conditions.
- `else` runs if no condition is true.
- Comparison operators compare values and return `True` or `False`.
- Logical operators combine multiple conditions.
- Decision-making is an important part of Python programming.