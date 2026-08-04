# Day 14 - Modules and Built-in Libraries

## 1. What is a module?

A module is a Python file that contains reusable functions, classes, and variables. Modules help organize code and avoid rewriting the same functionality.

Example:

```python
import math
```

---

## 2. What is a package?

A package is a collection of related Python modules stored in a folder. It helps organize larger projects.

Example:

```
mypackage/
│── calculator.py
│── shapes.py
│── __init__.py
```

---

## 3. How do you import a module?

You can import a module using the `import` keyword.

Examples:

```python
import math
import random
from datetime import datetime
```

---

## 4. What is the purpose of the `math` module?

The `math` module provides mathematical functions such as:

- `sqrt()` – Square root
- `pow()` – Power
- `ceil()` – Round up
- `floor()` – Round down

---

## 5. What is the purpose of the `random` module?

The `random` module generates random values.

Examples:

- `random.randint()` – Random integer
- `random.choice()` – Random item from a list

---

## 6. What is the purpose of the `datetime` module?

The `datetime` module is used to work with dates and times.

It can display:

- Current date
- Current time
- Year
- Month
- Day

---

## 7. Give two real-life examples where Python modules are useful.

### Example 1: Online Games

The `random` module is used to generate dice rolls, card shuffling, or random game events.

### Example 2: Banking Applications

The `datetime` module is used to record transaction dates and times.

---

# Key Points

- A module is a reusable Python file.
- A package is a collection of modules.
- `import` is used to include modules.
- `math` performs mathematical calculations.
- `random` generates random values.
- `datetime` works with dates and times.