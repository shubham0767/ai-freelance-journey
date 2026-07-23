# Day 03 - Python Operators

## 1. What is an Operator?

An operator is a symbol used to perform operations on variables and values.

Example:

```python
a = 10
b = 5
print(a + b)
```

Output:

```
15
```

---

## 2. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 10 + 5 = 15 |
| - | Subtraction | 10 - 5 = 5 |
| * | Multiplication | 10 * 5 = 50 |
| / | Division | 10 / 5 = 2.0 |
| // | Floor Division | 10 // 3 = 3 |
| % | Modulus (Remainder) | 10 % 3 = 1 |
| ** | Exponent (Power) | 2 ** 3 = 8 |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## 3. Comparison Operators

Comparison operators compare two values and return either True or False.

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example:

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

---

## 4. Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the result |

Example:

```python
age = 20
citizen = True

print(age >= 18 and citizen)
print(age >= 18 or citizen)
print(not citizen)
```

---

## 5. Assignment Operators

Assignment operators assign and update values.

| Operator | Example | Same As |
|----------|---------|---------|
| = | a = 10 | Assign value |
| += | a += 5 | a = a + 5 |
| -= | a -= 5 | a = a - 5 |
| *= | a *= 5 | a = a * 5 |
| /= | a /= 5 | a = a / 5 |
| %= | a %= 5 | a = a % 5 |

Example:

```python
num = 10

num += 5
print(num)

num -= 2
print(num)

num *= 3
print(num)
```

---

## 6. Operator Precedence

Operator precedence determines the order in which operations are performed.

Order:

1. ()
2. **
3. *, /, //, %
4. +, -
5. Comparison Operators
6. Logical Operators

Example:

```python
result = 5 + 2 * 3
print(result)
```

Output:

```
11
```

Because multiplication is performed before addition.

---

## Key Points

- Operators perform operations on values.
- Arithmetic operators are used for calculations.
- Comparison operators return True or False.
- Logical operators combine conditions.
- Assignment operators update variable values.
- Operator precedence decides the order of execution.

---

## Programs Completed Today

- arithmetic_operators.py
- comparison_operators.py
- logical_operators.py
- assignment_operators.py
- calculator_v2.py
- percentage_calculator.py

---

## What I Learned Today

- How to perform mathematical calculations in Python.
- How to compare values using comparison operators.
- How to combine conditions using logical operators.
- How to update variables using assignment operators.
- How Python follows operator precedence.
- How to build a simple calculator and percentage calculator.
