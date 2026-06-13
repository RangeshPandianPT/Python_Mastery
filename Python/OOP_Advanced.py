# =============================================================================
# ADVANCED OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON
# =============================================================================
# This file covers advanced OOP concepts building on the basics from OOP_Concepts.py

# =============================================================================
# 1. METHOD RESOLUTION ORDER (MRO)
# =============================================================================
# MRO determines the order in which base classes are searched when looking for a method

class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):  # Diamond inheritance
    pass

# MRO follows C3 Linearization algorithm
print(f"MRO of D: {D.__mro__}")
# Output: (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

d = D()
print(f"D.show(): {d.show()}")  # B (follows MRO: D -> B -> C -> A)

# Using super() properly with MRO
class Base:
    def __init__(self):
        print("Base init")

class Left(Base):
    def __init__(self):
        print("Left init")
        super().__init__()

class Right(Base):
    def __init__(self):
        print("Right init")
        super().__init__()

class Child(Left, Right):
    def __init__(self):
        print("Child init")
        super().__init__()

print("\nMRO chain demonstration:")
child = Child()  # Child -> Left -> Right -> Base (each called once!)


# =============================================================================
# 2. MIXINS
# =============================================================================
# Mixins are classes that provide methods to other classes via inheritance
# They are NOT meant to be instantiated directly

class JsonMixin:
    """Mixin to add JSON serialization capability"""
    import json
    
    def to_json(self):
        return self.json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls(**data)

class LoggingMixin:
    """Mixin to add logging capability"""
    def log(self, message):
        print(f"[LOG - {self.__class__.__name__}]: {message}")

class TimestampMixin:
    """Mixin to add timestamp capability"""
    from datetime import datetime
    
    def get_timestamp(self):
        return self.datetime.now().isoformat()

# Using multiple mixins
class User(JsonMixin, LoggingMixin, TimestampMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
user.log("User created")  # [LOG - User]: User created
print(f"JSON: {user.to_json()}")  # {"name": "Alice", "email": "alice@example.com"}
print(f"Timestamp: {user.get_timestamp()}")


# =============================================================================
# 3. DATACLASSES
# =============================================================================
# Dataclasses reduce boilerplate for classes that mainly store data

from dataclasses import dataclass, field
from typing import List

@dataclass
class Point:
    x: float
    y: float
    
    def distance_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

# Automatically generates __init__, __repr__, __eq__
p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)

print(f"Point: {p1}")           # Point(x=3.0, y=4.0)
print(f"p1 == p2: {p1 == p2}")  # True
print(f"Distance: {p1.distance_from_origin()}")  # 5.0

@dataclass(frozen=True)  # Immutable dataclass
class ImmutablePoint:
    x: float
    y: float

@dataclass
class GamePlayer:
    name: str
    level: int = 1  # Default value
    health: int = 100
    inventory: List[str] = field(default_factory=list)  # Mutable default
    
    def __post_init__(self):
        """Called after __init__"""
        if self.level < 1:
            raise ValueError("Level must be at least 1")

player = GamePlayer("Hero", level=5, inventory=["sword", "shield"])
print(f"Player: {player}")


# =============================================================================
# 4. __slots__ (Memory Optimization)
# =============================================================================
# __slots__ limits attributes and reduces memory usage

class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedClass:
    __slots__ = ['x', 'y']  # Only these attributes allowed
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

regular = RegularClass(1, 2)
slotted = SlottedClass(1, 2)

# Regular class has __dict__ (more memory)
print(f"Regular has __dict__: {hasattr(regular, '__dict__')}")  # True

# Slotted class has no __dict__ (less memory)
print(f"Slotted has __dict__: {hasattr(slotted, '__dict__')}")  # False

# Cannot add new attributes to slotted class
# slotted.z = 3  # AttributeError!

import sys
print(f"RegularClass dict size: {sys.getsizeof(regular.__dict__)} bytes")


# =============================================================================
# 5. CONTEXT MANAGERS (__enter__ and __exit__)
# =============================================================================
# Context managers handle setup and cleanup with 'with' statement

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening {self.filename}...")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block (even if exception occurs)"""
        print(f"Closing {self.filename}...")
        if self.file:
            self.file.close()
        # Return True to suppress exceptions, False to propagate
        return False

# Using the context manager
# with FileManager("test.txt", "w") as f:
#     f.write("Hello, World!")

# Using contextlib for simpler context managers
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    print("Timer started")
    yield  # Code inside 'with' block runs here
    end = time.time()
    print(f"Timer ended: {end - start:.4f} seconds")

# with timer():
#     sum([i**2 for i in range(1000000)])

print("Context Manager class created successfully!")


# =============================================================================
# 6. DESCRIPTORS
# =============================================================================
# Descriptors customize attribute access using __get__, __set__, __delete__

class Validator:
    """A descriptor that validates values"""
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        """Called when descriptor is assigned to a class attribute"""
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        obj.__dict__[self.name] = value

class Product:
    price = Validator(min_value=0)  # Price must be >= 0
    quantity = Validator(min_value=0, max_value=1000)  # 0-1000
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product = Product("Laptop", 999.99, 50)
print(f"Product: {product.name}, ${product.price}, Qty: {product.quantity}")

# product.price = -100  # ValueError: price must be >= 0


# =============================================================================
# 7. METACLASSES
# =============================================================================
# Metaclasses are "classes of classes" - they define how classes behave

# type is the default metaclass for all classes
print(f"Type of int: {type(int)}")      # <class 'type'>
print(f"Type of str: {type(str)}")      # <class 'type'>

# Creating a class dynamically using type
DynamicClass = type('DynamicClass', (object,), {'x': 10, 'greet': lambda self: 'Hello!'})
dynamic_obj = DynamicClass()
print(f"Dynamic object x: {dynamic_obj.x}, greet: {dynamic_obj.greet()}")

# Custom Metaclass
class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected to DB"
    
    def query(self, sql):
        return f"Executing: {sql}"

# Both variables reference the same instance
db1 = Database()
db2 = Database()
print(f"db1 is db2: {db1 is db2}")  # True (Singleton!)


# =============================================================================
# 8. CALLABLE OBJECTS (__call__)
# =============================================================================
# Making instances callable like functions

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5): {double(5)}")   # 10
print(f"triple(5): {triple(5)}")   # 15

# Practical example: Function decorator as a class
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))  # Call #1 to say_hello -> Hello, Alice!
print(say_hello("Bob"))    # Call #2 to say_hello -> Hello, Bob!


# =============================================================================
# 9. OPERATOR OVERLOADING (Advanced)
# =============================================================================
# Complete operator overloading example

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Arithmetic operators
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):  # Reverse multiplication (scalar * vector)
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
    # Comparison operators
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    
    def __le__(self, other):
        return self.magnitude() <= other.magnitude()
    
    # Unary operators
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        return self.magnitude()
    
    # Container/Sequence operators
    def __len__(self):
        return 2
    
    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        raise IndexError("Vector index out of range")
    
    def __iter__(self):
        yield self.x
        yield self.y
    
    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 + v2 = {v1 + v2}")      # Vector(4, 6)
print(f"v1 - v2 = {v1 - v2}")      # Vector(2, 2)
print(f"v1 * 3 = {v1 * 3}")        # Vector(9, 12)
print(f"3 * v1 = {3 * v1}")        # Vector(9, 12)
print(f"-v1 = {-v1}")              # Vector(-3, -4)
print(f"|v1| = {abs(v1)}")         # 5.0
print(f"v1[0], v1[1] = {v1[0]}, {v1[1]}")  # 3, 4
print(f"list(v1) = {list(v1)}")    # [3, 4]


# =============================================================================
# SUMMARY OF ADVANCED OOP CONCEPTS
# =============================================================================
"""
1. MRO: Method Resolution Order (C3 Linearization) for diamond inheritance
2. MIXINS: Reusable classes that provide methods to other classes
3. DATACLASSES: Reduced boilerplate for data-holding classes (@dataclass)
4. __slots__: Memory optimization by restricting instance attributes
5. CONTEXT MANAGERS: Setup/cleanup with __enter__ and __exit__
6. DESCRIPTORS: Custom attribute access with __get__, __set__, __delete__
7. METACLASSES: Classes that define how classes behave (Singleton example)
8. CALLABLE OBJECTS: Making instances callable with __call__
9. OPERATOR OVERLOADING: Complete customization of operators for custom types
"""

print("\n✅ Advanced OOP Concepts file created successfully!")
