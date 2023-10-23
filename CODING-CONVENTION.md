Python Coding Conventions
Introduction
This document outlines Python coding conventions to maintain consistency, readability, and collaboration across projects.

1. Indentation
Use 4 spaces for each level of indentation.
python
Copy code
# Good
def example_function():
    if condition:
        statement
2. Line Length
Keep lines of code to a maximum of 79 characters.
For comments and docstrings, the limit is 72 characters.
3. Imports
Imports should usually be on separate lines.
Standard library imports should be placed first.
Imports should be grouped and ordered by type (standard library, third-party, local).
python
Copy code
# Good
import os
import sys

import numpy as np
import pandas as pd

from my_module import my_function
4. Module-level Dunder Names
Use double underscores for module-level dunder (double underscore) names.
python
Copy code
# Good
__all__ = ['my_function']

__version__ = '1.0.0'
5. Whitespace in Expressions and Statements
Avoid extraneous whitespace within expressions and statements.
python
Copy code
# Good
spam(ham[1], {eggs: 2})

# Bad
spam( ham[ 1 ], { eggs: 2 } )
6. Comments
Use comments to explain non-obvious code and complex algorithms.
Write docstrings for functions, classes, and modules.
python
Copy code
# Good
def calculate_area(radius):
    """Calculate the area of a circle."""
    return 3.14159 * radius * radius
7. Naming Conventions
Use descriptive and meaningful names for variables, functions, and classes.
Use lowercase with underscores for function and variable names (snake_case).
Use CapWords for class names (CamelCase).
Constants should be in UPPERCASE.
python
Copy code
# Good
total_cost = 100
class MyClassName:
    ...

# Bad
x = 10
class myclassname:
    ...
8. String Quotes
Use single (' ') or double (" ") quotes consistently.
python
Copy code
# Good
name = 'Alice'
message = "Hello, World!"

# Bad
name = "Alice"
message = 'Hello, World!'
9. Trailing Commas
For lists, tuples, and function arguments, use trailing commas after the last element.
python
Copy code
# Good
fruits = ['apple', 'banana', 'cherry',]

# Bad
fruits = ['apple', 'banana', 'cherry']
10. Code Organization
Organize your code into logical blocks, functions, and classes.
Keep related functions and classes together in the same module.
11. Testing
Write unit tests using a framework like unittest or pytest.
