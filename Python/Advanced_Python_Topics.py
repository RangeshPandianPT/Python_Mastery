# ============================================================
# ADVANCED PYTHON TOPICS
# ============================================================
# This file covers important Python concepts including:
# - File Handling
# - Exception Handling
# - Decorators
# - Generators
# - Lambda Functions
# - List/Dict/Set Comprehensions
# - Context Managers
# ============================================================


# ============================================================
# 1. EXCEPTION HANDLING
# ============================================================
"""
Exception handling allows you to handle errors gracefully
without crashing the program.

Keywords:
- try: Block of code to test
- except: Handle the exception
- else: Executes if no exception
- finally: Always executes
"""

# Basic Exception Handling
print("=" * 50)
print("EXCEPTION HANDLING")
print("=" * 50)

# Example 1: Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Example 2: Multiple except blocks
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except IndexError:
    print("Error: Index out of range!")
except TypeError:
    print("Error: Type mismatch!")

# Example 3: Catching multiple exceptions in one block
try:
    value = int("hello")
except (ValueError, TypeError) as e:
    print(f"Error occurred: {e}")

# Example 4: Using else and finally
try:
    num = int("42")
except ValueError:
    print("Invalid number!")
else:
    print(f"Conversion successful: {num}")
finally:
    print("This always runs!")

# Example 5: Raising custom exceptions
class CustomError(Exception):
    """Custom exception class"""
    pass

def check_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative!")
    return f"Age is: {age}"

try:
    print(check_age(-5))
except CustomError as e:
    print(f"Custom Error: {e}")


# ============================================================
# 2. FILE HANDLING
# ============================================================
"""
Python provides built-in functions to work with files.

Modes:
- 'r': Read (default)
- 'w': Write (overwrites file)
- 'a': Append
- 'x': Create (fails if exists)
- 'b': Binary mode
- 't': Text mode (default)
- 'r+': Read and Write
"""

print("\n" + "=" * 50)
print("FILE HANDLING")
print("=" * 50)

# Example 1: Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy.\n")
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
print("File written successfully!")

# Example 2: Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Example 3: Reading line by line
with open("sample.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(f"  -> {line.strip()}")

# Example 4: Reading into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")

# Example 5: Appending to a file
with open("sample.txt", "a") as file:
    file.write("This line was appended!\n")

# Example 6: Working with file positions
with open("sample.txt", "r") as file:
    print(f"Current position: {file.tell()}")
    file.read(5)
    print(f"After reading 5 chars: {file.tell()}")
    file.seek(0)  # Go back to start
    print(f"After seek(0): {file.tell()}")


# ============================================================
# 3. LAMBDA FUNCTIONS
# ============================================================
"""
Lambda functions are small anonymous functions.
Syntax: lambda arguments: expression
"""

print("\n" + "=" * 50)
print("LAMBDA FUNCTIONS")
print("=" * 50)

# Example 1: Basic lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Example 2: Lambda with multiple arguments
add = lambda a, b: a + b
print(f"5 + 3 = {add(5, 3)}")

# Example 3: Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Example 4: Lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Example 5: Lambda with sorted()
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by grade: {sorted_students}")

# Example 6: Lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"Product: {product}")


# ============================================================
# 4. COMPREHENSIONS
# ============================================================
"""
Comprehensions provide a concise way to create collections.
"""

print("\n" + "=" * 50)
print("COMPREHENSIONS")
print("=" * 50)

# List Comprehension
# Syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Dictionary Comprehension
# Syntax: {key: value for item in iterable if condition}
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dict: {square_dict}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# Set Comprehension
# Syntax: {expression for item in iterable if condition}
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
print(f"Unique squares: {unique_squares}")

# Generator Expression (memory efficient)
# Syntax: (expression for item in iterable if condition)
gen = (x**2 for x in range(1, 6))
print(f"Generator: {gen}")
print(f"Generator values: {list(gen)}")


# ============================================================
# 5. DECORATORS
# ============================================================
"""
Decorators are functions that modify the behavior of other functions.
They use the @decorator syntax.
"""

print("\n" + "=" * 50)
print("DECORATORS")
print("=" * 50)

# Example 1: Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Example 2: Decorator with arguments
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_args
def add_numbers(a, b):
    return a + b

print(f"Result: {add_numbers(3, 5)}")

# Example 3: Timing decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done!"

print(slow_function())

# Example 4: Decorator with parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return name

greet("Python")

# Example 5: Class-based decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_bye():
    print("Goodbye!")

say_bye()
say_bye()


# ============================================================
# 6. GENERATORS
# ============================================================
"""
Generators are functions that yield values one at a time,
making them memory efficient for large datasets.
"""

print("\n" + "=" * 50)
print("GENERATORS")
print("=" * 50)

# Example 1: Basic generator
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

counter = count_up_to(5)
print(f"Generator object: {counter}")
print(f"Values: {list(count_up_to(5))}")

# Example 2: Using next()
gen = count_up_to(3)
print(f"First: {next(gen)}")
print(f"Second: {next(gen)}")
print(f"Third: {next(gen)}")

# Example 3: Infinite generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(f"Infinite gen samples: {[next(gen) for _ in range(5)]}")

# Example 4: Generator for fibonacci
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print(f"Fibonacci: {list(fibonacci(100))}")

# Example 5: Generator pipeline
def numbers(n):
    for i in range(n):
        yield i

def squared(seq):
    for num in seq:
        yield num ** 2

def even_only(seq):
    for num in seq:
        if num % 2 == 0:
            yield num

# Chaining generators
pipeline = even_only(squared(numbers(10)))
print(f"Pipeline result: {list(pipeline)}")


# ============================================================
# 7. CONTEXT MANAGERS
# ============================================================
"""
Context managers allow you to allocate and release resources precisely.
They use the 'with' statement.
"""

print("\n" + "=" * 50)
print("CONTEXT MANAGERS")
print("=" * 50)

# Example 1: Using contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    yield name
    print(f"Releasing {name}")

with managed_resource("Database Connection") as resource:
    print(f"Using {resource}")

# Example 2: Class-based context manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("File closed properly!")

with FileManager("test.txt", "w") as f:
    f.write("Using custom context manager!")

# Example 3: Multiple context managers
with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("Content for file 1")
    f2.write("Content for file 2")


# ============================================================
# 8. USEFUL BUILT-IN FUNCTIONS
# ============================================================
"""
Python has many useful built-in functions.
"""

print("\n" + "=" * 50)
print("USEFUL BUILT-IN FUNCTIONS")
print("=" * 50)

# zip() - Combine iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(f"Zipped: {combined}")

# enumerate() - Add index to iterable
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# any() and all()
numbers = [1, 2, 3, 0, 5]
print(f"Any truthy: {any(numbers)}")  # True
print(f"All truthy: {all(numbers)}")  # False (0 is falsy)

# min() and max() with key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
top_student = max(students, key=lambda x: x[1])
print(f"Top student: {top_student}")

# isinstance() and type()
x = 42
print(f"Is int: {isinstance(x, int)}")
print(f"Type: {type(x)}")

# getattr(), setattr(), hasattr()
class MyClass:
    name = "Python"

obj = MyClass()
print(f"Has name: {hasattr(obj, 'name')}")
print(f"Get name: {getattr(obj, 'name')}")
setattr(obj, 'version', 3.9)
print(f"Version: {obj.version}")

# eval() and exec() - Use with caution!
result = eval("2 + 3 * 4")
print(f"Eval result: {result}")


# ============================================================
# SUMMARY
# ============================================================
"""
Key Takeaways:

1. EXCEPTION HANDLING
   - Use try/except for error handling
   - finally block always executes
   - Create custom exceptions when needed

2. FILE HANDLING
   - Always use 'with' for automatic cleanup
   - Different modes: r, w, a, x, b, t

3. LAMBDA FUNCTIONS
   - Small anonymous functions
   - Great with map(), filter(), sorted()

4. COMPREHENSIONS
   - List: [expr for item in iterable if cond]
   - Dict: {k: v for item in iterable if cond}
   - Set: {expr for item in iterable if cond}

5. DECORATORS
   - Modify function behavior
   - Use @decorator syntax
   - Can have parameters

6. GENERATORS
   - Use yield instead of return
   - Memory efficient
   - Great for large datasets

7. CONTEXT MANAGERS
   - Use 'with' statement
   - Automatic resource management
   - Implement __enter__ and __exit__
"""

print("\n" + "=" * 50)
print("Advanced Python Topics Complete!")
print("=" * 50)

# Cleanup: Remove sample files created during examples
import os
for filename in ["sample.txt", "test.txt", "file1.txt", "file2.txt"]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Cleaned up: {filename}")
