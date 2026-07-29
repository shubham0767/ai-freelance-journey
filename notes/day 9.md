# Day 09 - Strings in Python

## 1. What is a string?

A string is a sequence of characters enclosed in single quotes (' ') or double quotes (" "). Strings are used to store text such as names, messages, and passwords.

Example:

```python
name = "Shubham"
```

---

## 2. What is string indexing?

String indexing is used to access individual characters in a string. Indexing starts from 0.

Example:

```python
text = "Python"

print(text[0])   # P
print(text[1])   # y
print(text[-1])  # n
```

---

## 3. What is string slicing?

String slicing is used to extract a part of a string using the format:

```python
string[start:end]
```

Example:

```python
text = "Python"

print(text[0:3])   # Pyt
print(text[2:])    # thon
```

---

## 4. What do upper(), lower(), title(), and split() do?

- `upper()` converts all letters to uppercase.
- `lower()` converts all letters to lowercase.
- `title()` converts the first letter of each word to uppercase.
- `split()` splits a sentence into a list of words.

Example:

```python
text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())

words = text.split()
print(words)
```

---

## 5. How do you reverse a string?

A string can be reversed using slicing.

Example:

```python
text = "Python"

print(text[::-1])
```

Output:

```
nohtyP
```

---

## 6. Give two real-life examples where strings are useful.

### Example 1: Login System

Usernames, email addresses, and passwords are stored as strings.

### Example 2: Chat Application

Messages sent between users are stored and processed as strings.

---

# Key Points

- A string is a sequence of characters.
- Indexing starts from 0.
- Slicing extracts part of a string.
- `upper()`, `lower()`, `title()`, and `split()` are common string methods.
- `[::-1]` reverses a string.
- Strings are widely used in Python, web development, and AI.