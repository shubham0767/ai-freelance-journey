1. What is a Python module?

A Python module is a Python file (.py) that contains reusable code such as functions, variables, and classes.

Example:

# calculator.py

def add(a, b):
    return a + b

We can use it in another file:

import calculator

print(calculator.add(10, 20))
2. What is a Python package?

A Python package is a folder that contains related Python modules.

Example:

math_tools/
├── __init__.py
├── calculator.py
└── numbers.py

Packages help organize larger projects.

3. What is the difference between import and from ... import?

import imports the entire module:

import calculator

calculator.add(10, 20)

from ... import imports specific functions, classes, or variables:

from calculator import add

add(10, 20)

So, import gives access through the module name, while from ... import lets you use the selected item directly.

4. What is pip?

pip is Python's package installer. It is used to install and manage Python packages and third-party libraries.

Example:

pip install requests
5. What does pip install do?

pip install downloads and installs a Python package and its required dependencies into your Python environment.

Example:

pip install requests

This installs the requests library.

6. What is a third-party library?

A third-party library is a library developed separately from Python's standard library and made available for developers to install and use.

Examples:

requests
numpy
pandas
flask

They provide functionality that you can reuse instead of writing everything yourself.

7. What is requirements.txt?

requirements.txt is a text file that lists the packages required by a Python project.

Example:

requests
flask
numpy

You can install all the listed packages with:

pip install -r requirements.txt
8. Why are modules useful in large projects?

Modules help developers:

Organize code into separate files.
Reuse functions and classes.
Make code easier to understand.
Make debugging and maintenance easier.

For example:

project/
├── database.py
├── login.py
├── calculator.py
└── main.py

Instead of putting everything into one huge file.

9. Why are packages useful?

Packages group related modules together and provide a clean structure for large applications.

For example:

project/
├── users/
│   ├── login.py
│   └── registration.py
│
└── payments/
    ├── card.py
    └── upi.py

This makes large projects easier to organize and maintain.

10. Give two examples of Python libraries you have used.

Two examples from today's practice are:

Requests — used for making HTTP requests and communicating with web APIs.
Math — provides mathematical functions such as square root, ceiling, floor, and powers.

Note: math is actually part of Python's standard library, so it isn't a third-party library. requests is a third-party library.