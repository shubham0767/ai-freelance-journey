# Day 17 - Iterators, Generators, and Virtual Environments

## 1. What is an iterator?

An iterator is an object that allows you to access elements of a collection one at a time using the `next()` function.

Example:

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
```

---

## 2. What is the difference between an iterable and an iterator?

| Iterable | Iterator |
|----------|----------|
| Can be looped over | Produces one value at a time |
| Examples: list, tuple, string | Created using `iter()` |
| Does not remember current position | Remembers its current position |

---

## 3. What is a generator?

A generator is a special function that uses the `yield` keyword to produce values one at a time instead of returning them all at once.

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

---

## 4. What is the purpose of the `yield` keyword?

The `yield` keyword returns one value at a time and pauses the function. When called again, it continues from where it stopped.

---

## 5. What are the advantages of generators?

- Use less memory.
- Generate values only when needed.
- Suitable for large datasets.
- Improve performance for sequential processing.

---

## 6. What is a virtual environment?

A virtual environment is an isolated Python environment that keeps project dependencies separate from other projects.

---

## 7. Why do Python developers use virtual environments?

- To avoid dependency conflicts.
- To keep project packages organized.
- To allow different projects to use different package versions.

---

## 8. Give two real-life examples where generators are useful.

### Example 1: Reading Large Log Files

A generator reads one line at a time instead of loading the entire file into memory.

### Example 2: Streaming Data

Generators can process live data, such as sensor readings or online data streams, without storing everything at once.

---

# Key Points

- Iterators return one element at a time using `next()`.
- Iterables can be converted into iterators with `iter()`.
- Generators use `yield` to produce values one by one.
- Generators are memory efficient.
- Virtual environments isolate project dependencies.