# ============================================================
# IMPORTANT PYTHON LIBRARIES
# ============================================================
# This file covers essential Python libraries including:
# - os & sys (System Operations)
# - datetime (Date & Time)
# - math & random (Mathematics)
# - json (Data Serialization)
# - re (Regular Expressions)
# - collections (Advanced Data Structures)
# - itertools (Iteration Tools)
# - requests (HTTP Requests) [Third-party]
# - pandas basics [Third-party]
# ============================================================


# ============================================================
# 1. OS MODULE - Operating System Interface
# ============================================================
"""
The os module provides functions to interact with the operating system.
"""

import os

print("=" * 50)
print("OS MODULE")
print("=" * 50)

# Current working directory
print(f"Current directory: {os.getcwd()}")

# List directory contents
print(f"Directory contents: {os.listdir('.')[:5]}...")  # First 5 items

# Path operations
print(f"User home: {os.path.expanduser('~')}")
print(f"Join paths: {os.path.join('folder', 'subfolder', 'file.txt')}")
print(f"File exists: {os.path.exists('Python_Libraries.py')}")
print(f"Is directory: {os.path.isdir('.')}")
print(f"Is file: {os.path.isfile('Python_Libraries.py')}")

# Path manipulation
path = "/home/user/documents/file.txt"
print(f"Basename: {os.path.basename(path)}")  # file.txt
print(f"Dirname: {os.path.dirname(path)}")    # /home/user/documents
print(f"Split: {os.path.split(path)}")        # ('/home/user/documents', 'file.txt')
print(f"Extension: {os.path.splitext(path)}") # ('/home/user/documents/file', '.txt')

# Environment variables
print(f"PATH: {os.environ.get('PATH', 'Not found')[:50]}...")

# Creating and removing directories
# os.mkdir('new_folder')      # Create directory
# os.makedirs('a/b/c')        # Create nested directories
# os.rmdir('new_folder')      # Remove empty directory
# os.remove('file.txt')       # Remove file


# ============================================================
# 2. SYS MODULE - System-specific Parameters
# ============================================================
"""
The sys module provides access to Python interpreter variables.
"""

import sys

print("\n" + "=" * 50)
print("SYS MODULE")
print("=" * 50)

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Executable path: {sys.executable}")
print(f"Module search paths: {sys.path[:3]}...")
print(f"Command line args: {sys.argv}")
print(f"Max integer size: {sys.maxsize}")
print(f"Default encoding: {sys.getdefaultencoding()}")

# Memory size of object
x = [1, 2, 3, 4, 5]
print(f"Size of list: {sys.getsizeof(x)} bytes")


# ============================================================
# 3. DATETIME MODULE - Date and Time
# ============================================================
"""
The datetime module provides classes for working with dates and times.
"""

from datetime import datetime, date, time, timedelta

print("\n" + "=" * 50)
print("DATETIME MODULE")
print("=" * 50)

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Current date: {date.today()}")

# Creating specific dates
specific_date = datetime(2024, 12, 25, 10, 30, 0)
print(f"Christmas 2024: {specific_date}")

# Accessing components
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Weekday: {now.weekday()}")  # 0=Monday, 6=Sunday

# Formatting dates
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Custom format: {now.strftime('%B %d, %Y')}")  # January 12, 2024

# Parsing strings to dates
date_str = "2024-06-15"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")

# Date arithmetic with timedelta
future = now + timedelta(days=30)
past = now - timedelta(weeks=2)
print(f"30 days from now: {future.date()}")
print(f"2 weeks ago: {past.date()}")

# Difference between dates
diff = future - now
print(f"Difference: {diff.days} days")


# ============================================================
# 4. MATH MODULE - Mathematical Functions
# ============================================================
"""
The math module provides mathematical functions and constants.
"""

import math

print("\n" + "=" * 50)
print("MATH MODULE")
print("=" * 50)

# Constants
print(f"Pi: {math.pi}")
print(f"Euler's number (e): {math.e}")
print(f"Infinity: {math.inf}")

# Basic functions
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Power 2^10: {math.pow(2, 10)}")
print(f"Absolute value: {math.fabs(-5.5)}")

# Rounding functions
print(f"Ceiling of 4.3: {math.ceil(4.3)}")   # 5
print(f"Floor of 4.7: {math.floor(4.7)}")    # 4
print(f"Truncate 4.7: {math.trunc(4.7)}")    # 4

# Trigonometric functions (radians)
print(f"Sin(90°): {math.sin(math.radians(90))}")
print(f"Cos(0°): {math.cos(math.radians(0))}")

# Logarithmic functions
print(f"Log base e: {math.log(10)}")
print(f"Log base 10: {math.log10(100)}")
print(f"Log base 2: {math.log2(8)}")

# Other useful functions
print(f"Factorial of 5: {math.factorial(5)}")
print(f"GCD of 48, 18: {math.gcd(48, 18)}")
print(f"LCM of 4, 6: {math.lcm(4, 6)}")


# ============================================================
# 5. RANDOM MODULE - Random Number Generation
# ============================================================
"""
The random module provides functions for generating random numbers.
"""

import random

print("\n" + "=" * 50)
print("RANDOM MODULE")
print("=" * 50)

# Random float between 0 and 1
print(f"Random float: {random.random()}")

# Random float in range
print(f"Random between 1-10: {random.uniform(1, 10)}")

# Random integer
print(f"Random int 1-100: {random.randint(1, 100)}")

# Random choice from sequence
colors = ["red", "green", "blue", "yellow"]
print(f"Random color: {random.choice(colors)}")

# Multiple random choices
print(f"3 random colors: {random.choices(colors, k=3)}")

# Random sample (no duplicates)
print(f"Sample 2 colors: {random.sample(colors, 2)}")

# Shuffle list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled: {numbers}")

# Setting seed for reproducibility
random.seed(42)
print(f"Seeded random: {random.random()}")


# ============================================================
# 6. JSON MODULE - JSON Data Handling
# ============================================================
"""
The json module provides functions for encoding and decoding JSON data.
"""

import json

print("\n" + "=" * 50)
print("JSON MODULE")
print("=" * 50)

# Python dict to JSON string
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JavaScript"],
    "active": True
}

json_string = json.dumps(data, indent=2)
print(f"JSON string:\n{json_string}")

# JSON string to Python dict
parsed_data = json.loads(json_string)
print(f"Parsed back: {parsed_data}")
print(f"Name: {parsed_data['name']}")

# Writing JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
print("JSON saved to file!")

# Reading JSON from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print(f"Loaded from file: {loaded_data}")

# Cleanup
os.remove("data.json")


# ============================================================
# 7. RE MODULE - Regular Expressions
# ============================================================
"""
The re module provides regular expression matching operations.
"""

import re

print("\n" + "=" * 50)
print("RE MODULE (Regular Expressions)")
print("=" * 50)

text = "Contact us at support@email.com or sales@company.org"

# Find all matches
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(f"Emails found: {emails}")

# Search for pattern (first match)
match = re.search(r'\d+', "Order #12345 confirmed")
if match:
    print(f"Order number: {match.group()}")

# Match at beginning
if re.match(r'Hello', "Hello World"):
    print("String starts with 'Hello'")

# Replace pattern
new_text = re.sub(r'\d+', 'XXX', "Phone: 123-456-7890")
print(f"Censored: {new_text}")

# Split by pattern
parts = re.split(r'[,;]', "apple,banana;cherry,date")
print(f"Split result: {parts}")

# Compile pattern for reuse
pattern = re.compile(r'\b[A-Z][a-z]+\b')
names = pattern.findall("John met Alice and Bob")
print(f"Names found: {names}")

# Using groups
phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
match = re.search(phone_pattern, "Call: 123-456-7890")
if match:
    print(f"Area code: {match.group(1)}")
    print(f"Full number: {match.group(0)}")


# ============================================================
# 8. COLLECTIONS MODULE - Specialized Data Types
# ============================================================
"""
The collections module provides specialized container datatypes.
"""

from collections import Counter, defaultdict, namedtuple, deque, OrderedDict

print("\n" + "=" * 50)
print("COLLECTIONS MODULE")
print("=" * 50)

# Counter - Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(f"Word counts: {counter}")
print(f"Most common: {counter.most_common(2)}")

# defaultdict - Dictionary with default values
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
dd['vegetables'].append('carrot')
print(f"defaultdict: {dict(dd)}")

# With int default
word_count = defaultdict(int)
for word in "hello world hello".split():
    word_count[word] += 1
print(f"Word count: {dict(word_count)}")

# namedtuple - Named tuples
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: {p}")
print(f"X: {p.x}, Y: {p.y}")

# deque - Double-ended queue
dq = deque([1, 2, 3])
dq.append(4)       # Add to right
dq.appendleft(0)   # Add to left
print(f"Deque: {dq}")
dq.pop()           # Remove from right
dq.popleft()       # Remove from left
print(f"After pops: {dq}")

# Rotate deque
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)       # Rotate right
print(f"Rotated: {dq}")


# ============================================================
# 9. ITERTOOLS MODULE - Iteration Utilities
# ============================================================
"""
The itertools module provides efficient iteration tools.
"""

import itertools

print("\n" + "=" * 50)
print("ITERTOOLS MODULE")
print("=" * 50)

# count - Infinite counter
counter = itertools.count(start=1, step=2)
print(f"Count odds: {[next(counter) for _ in range(5)]}")

# cycle - Cycle through iterable
cycler = itertools.cycle(['A', 'B', 'C'])
print(f"Cycle: {[next(cycler) for _ in range(7)]}")

# repeat - Repeat value
print(f"Repeat: {list(itertools.repeat('Hello', 3))}")

# chain - Combine iterables
combined = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(f"Chained: {combined}")

# permutations
perms = list(itertools.permutations([1, 2, 3], 2))
print(f"Permutations: {perms}")

# combinations
combs = list(itertools.combinations([1, 2, 3, 4], 2))
print(f"Combinations: {combs}")

# combinations with replacement
combs_rep = list(itertools.combinations_with_replacement([1, 2], 3))
print(f"Combinations with replacement: {combs_rep}")

# product - Cartesian product
prod = list(itertools.product([1, 2], ['a', 'b']))
print(f"Product: {prod}")

# groupby - Group consecutive elements
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {list(group)}")

# accumulate - Running totals
nums = [1, 2, 3, 4, 5]
print(f"Accumulate: {list(itertools.accumulate(nums))}")


# ============================================================
# 10. FUNCTOOLS MODULE - Higher-Order Functions
# ============================================================
"""
The functools module provides tools for working with functions.
"""

from functools import reduce, partial, lru_cache, wraps

print("\n" + "=" * 50)
print("FUNCTOOLS MODULE")
print("=" * 50)

# reduce - Apply function cumulatively
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product using reduce: {product}")

# partial - Freeze some function arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(f"Square of 5: {square(5)}")
print(f"Cube of 3: {cube(3)}")

# lru_cache - Memoization
@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(30): {fibonacci(30)}")
print(f"Cache info: {fibonacci.cache_info()}")

# wraps - Preserve function metadata in decorators
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example_func():
    """This is an example function."""
    pass

print(f"Function name: {example_func.__name__}")
print(f"Docstring: {example_func.__doc__}")


# ============================================================
# 11. LOGGING MODULE - Application Logging
# ============================================================
"""
The logging module provides flexible logging capabilities.
"""

import logging

print("\n" + "=" * 50)
print("LOGGING MODULE")
print("=" * 50)

# Configure basic logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s'
)

# Different log levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


# ============================================================
# 12. THREADING MODULE - Concurrent Execution
# ============================================================
"""
The threading module provides thread-based parallelism.
"""

import threading
import time

print("\n" + "=" * 50)
print("THREADING MODULE")
print("=" * 50)

def worker(name, delay):
    print(f"Thread {name} starting")
    time.sleep(delay)
    print(f"Thread {name} finished")

# Create threads
thread1 = threading.Thread(target=worker, args=("A", 0.1))
thread2 = threading.Thread(target=worker, args=("B", 0.1))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads completed!")


# ============================================================
# 13. REQUESTS MODULE (Third-Party) - HTTP Requests
# ============================================================
"""
The requests library simplifies making HTTP requests.
Install: pip install requests
"""

print("\n" + "=" * 50)
print("REQUESTS MODULE (Third-Party)")
print("=" * 50)

# Note: Uncomment to use (requires: pip install requests)
"""
import requests

# GET request
response = requests.get('https://api.github.com')
print(f"Status: {response.status_code}")
print(f"Headers: {response.headers['content-type']}")
print(f"JSON: {response.json()}")

# GET with parameters
params = {'q': 'python', 'page': 1}
response = requests.get('https://api.github.com/search/repositories', params=params)

# POST request
data = {'name': 'John', 'age': 30}
response = requests.post('https://httpbin.org/post', json=data)

# Headers and authentication
headers = {'Authorization': 'Bearer token123'}
response = requests.get('https://api.example.com', headers=headers)

# Timeout and error handling
try:
    response = requests.get('https://api.example.com', timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
"""
print("(Uncomment code to use - requires 'pip install requests')")


# ============================================================
# 14. PATHLIB MODULE - Object-Oriented Path Handling
# ============================================================
"""
The pathlib module provides object-oriented filesystem paths.
"""

from pathlib import Path

print("\n" + "=" * 50)
print("PATHLIB MODULE")
print("=" * 50)

# Current directory
current = Path.cwd()
print(f"Current dir: {current}")

# Home directory
home = Path.home()
print(f"Home dir: {home}")

# Creating paths
path = Path("folder") / "subfolder" / "file.txt"
print(f"Joined path: {path}")

# Path components
p = Path("/home/user/documents/file.txt")
print(f"Name: {p.name}")           # file.txt
print(f"Stem: {p.stem}")           # file
print(f"Suffix: {p.suffix}")       # .txt
print(f"Parent: {p.parent}")       # /home/user/documents
print(f"Parts: {p.parts}")         # ('/', 'home', 'user', 'documents', 'file.txt')

# Check path properties
script_path = Path(__file__) if '__file__' in dir() else Path(".")
print(f"Exists: {script_path.exists()}")
print(f"Is file: {script_path.is_file()}")
print(f"Is dir: {script_path.is_dir()}")

# List directory contents
for item in Path(".").iterdir():
    if item.suffix == ".py":
        print(f"  Python file: {item.name}")

# Glob patterns
python_files = list(Path(".").glob("*.py"))
print(f"Python files count: {len(python_files)}")


# ============================================================
# SUMMARY
# ============================================================
"""
Key Python Libraries:

STANDARD LIBRARY:
├── os          - Operating system interface
├── sys         - System-specific parameters  
├── datetime    - Date and time operations
├── math        - Mathematical functions
├── random      - Random number generation
├── json        - JSON encoding/decoding
├── re          - Regular expressions
├── collections - Specialized containers
├── itertools   - Iteration utilities
├── functools   - Higher-order functions
├── logging     - Application logging
├── threading   - Concurrent execution
└── pathlib     - Object-oriented paths

POPULAR THIRD-PARTY:
├── requests    - HTTP requests (pip install requests)
├── numpy       - Numerical computing (pip install numpy)
├── pandas      - Data analysis (pip install pandas)
├── matplotlib  - Data visualization (pip install matplotlib)
└── flask/django - Web frameworks

Installation:
  pip install <package_name>
  pip install -r requirements.txt
"""

print("\n" + "=" * 50)
print("Python Libraries Overview Complete!")
print("=" * 50)
