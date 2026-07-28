"""
SOLID Principles in Python
==========================

This file provides a brief summary and code examples of the 5 SOLID principles.

S - Single Responsibility Principle (SRP)
O - Open/Closed Principle (OCP)
L - Liskov Substitution Principle (LSP)
I - Interface Segregation Principle (ISP)
D - Dependency Inversion Principle (DIP)
"""

from abc import ABC, abstractmethod

# ---------------------------------------------------------
# 1. Single Responsibility Principle (SRP)
# A class should have one, and only one, reason to change.
# ---------------------------------------------------------
class ReportGenerator:
    def generate_report(self, data):
        # Generates report data
        return f"Report: {data}"

class ReportSaver:
    def save_to_file(self, content, filename):
        # Handles saving
        with open(filename, 'w') as f:
            f.write(content)

# ---------------------------------------------------------
# 2. Open/Closed Principle (OCP)
# Software entities should be open for extension, but closed for modification.
# ---------------------------------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * (self.radius ** 2)

def calculate_area(shapes: list[Shape]):
    # Open for extension (can add new shapes without modifying this function)
    return sum([shape.area() for shape in shapes])

# ---------------------------------------------------------
# 3. Liskov Substitution Principle (LSP)
# Objects in a program should be replaceable with instances of their subtypes without altering the correctness.
# ---------------------------------------------------------
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "I am flying"

class Ostrich(Bird):
    # Ostrich cannot fly, so extending a general 'Bird' with a fly() method violates LSP.
    def move(self):
        return "I am running"

# ---------------------------------------------------------
# 4. Interface Segregation Principle (ISP)
# Many client-specific interfaces are better than one general-purpose interface.
# ---------------------------------------------------------
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing...")
    def scan_document(self):
        print("Scanning...")

class SimplePrinter(Printer):
    def print_document(self):
        print("Printing...")
    # Does not need to implement scan_document()

# ---------------------------------------------------------
# 5. Dependency Inversion Principle (DIP)
# Depend upon abstractions, not concretions.
# ---------------------------------------------------------
class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleLogger(LoggerInterface):
    def log(self, message: str):
        print(f"Log: {message}")

class App:
    def __init__(self, logger: LoggerInterface): # Depends on abstraction
        self.logger = logger

    def run(self):
        self.logger.log("App is running")
