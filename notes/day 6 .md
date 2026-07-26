# Day 06 - Functions in Python

## 1. What is a function?

A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we write it once inside a function and call it whenever needed.

### Example

```python
def greet():
    print("Welcome to Python!")

greet()
```

**Output:**

```
Welcome to Python!
```

---

## 2. Why do we use functions?

Functions make programs easier to write, read, and maintain.

### Advantages of Functions

- Avoid repeating the same code.
- Make the program organized and readable.
- Save development time.
- Make debugging easier.
- Allow code to be reused in different parts of a program.

### Example

Instead of writing the addition code many times, create one function:

```python
def add(a, b):
    return a + b
```

Now you can call it whenever you need:

```python
print(add(10, 20))
print(add(50, 30))
```

---

## 3. What is the difference between a parameter and an argument?

### Parameter

A **parameter** is a variable written in the function definition. It acts as a placeholder for the value that will be passed to the function.

Example:

```python
def add(a, b):
    return a + b
```

Here, `a` and `b` are **parameters**.

### Argument

An **argument** is the actual value passed to the function when it is called.

Example:

```python
add(10, 20)
```

Here, `10` and `20` are **arguments**.

### Summary

| Parameter | Argument |
|-----------|----------|
| Defined in the function | Passed when calling the function |
| Acts as a placeholder | Actual value |

---

## 4. What is the `return` keyword?

The `return` keyword sends a value back from a function to the place where it was called.

### Example

```python
def square(num):
    return num * num

result = square(5)

print(result)
```

**Output:**

```
25
```

Without `return`, the function cannot send a value back to the caller.

---

## 5. What is the difference between `print()` and `return()`?

### `print()`

- Displays the output on the screen.
- Does not send the value back to the caller.

Example:

```python
def greet():
    print("Hello")

greet()
```

### `return`

- Sends a value back from the function.
- The returned value can be stored in a variable or used in another calculation.

Example:

```python
def add(a, b):
    return a + b

answer = add(5, 10)

print(answer)
```

### Difference

| print() | return |
|----------|---------|
| Displays output | Sends a value back |
| Cannot be reused easily | Returned value can be stored and reused |
| Mainly for showing results | Mainly for calculations and further processing |

---

## 6. Give two real-life examples where functions are useful.

### Example 1: ATM Machine

An ATM has separate functions such as:

- Check Balance
- Withdraw Money
- Deposit Money
- Change PIN

Each task is performed by a different function.

### Example 2: Online Shopping App

An online shopping application uses functions like:

- Login User
- Search Product
- Add to Cart
- Calculate Total Price
- Make Payment

Each function performs one specific task, making the application organized and easy to manage.

---

# Key Points

- A function is a reusable block of code.
- Functions reduce code duplication.
- Parameters receive values inside the function.
- Arguments are the actual values passed to the function.
- `return` sends a value back to the caller.
- `print()` displays output, while `return` provides a value for further use.
- Functions make programs clean, modular, and easier to maintain.