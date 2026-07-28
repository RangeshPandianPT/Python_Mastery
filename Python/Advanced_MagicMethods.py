"""
Advanced Python Magic Methods, Descriptors, and Context Managers
================================================================
"""
from typing import Any

# ---------------------------------------------------------
# 1. Descriptors
# A descriptor is an object attribute with "binding behavior", one whose 
# attribute access has been overridden by methods in the descriptor protocol:
# __get__(), __set__(), and __delete__().
# ---------------------------------------------------------
class ValidatedProperty:
    def __init__(self, min_value=None):
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.public_name} must be at least {self.min_value}")
        setattr(obj, self.private_name, value)

class Product:
    price = ValidatedProperty(min_value=0) # Must be >= 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

# ---------------------------------------------------------
# 2. Metaclasses
# Metaclasses are classes whose instances are classes.
# ---------------------------------------------------------
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing database...")

# ---------------------------------------------------------
# 3. Context Managers (Custom)
# ---------------------------------------------------------
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start:.4f} seconds")

if __name__ == "__main__":
    print("--- Descriptors ---")
    p = Product("Laptop", 1200)
    print(f"Price: {p.price}")
    try:
        p.price = -10
    except ValueError as e:
        print(f"Caught Error: {e}")

    print("\n--- Metaclasses ---")
    d1 = Database()
    d2 = Database()
    print(f"d1 is d2? {d1 is d2}")

    print("\n--- Context Managers ---")
    with Timer():
        import time
        time.sleep(0.5)
