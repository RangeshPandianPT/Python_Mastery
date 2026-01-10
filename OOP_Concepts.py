# =============================================================================
# OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON
# =============================================================================
# OOP is a programming paradigm that organizes code into objects containing
# data (attributes) and behavior (methods)

# =============================================================================
# 1. CLASSES AND OBJECTS
# =============================================================================
# Class: A blueprint/template for creating objects
# Object: An instance of a class

class Car:
    """A simple Car class"""
    pass  # Empty class

# Creating objects (instances)
my_car = Car()
your_car = Car()

print(f"my_car is an instance of Car: {isinstance(my_car, Car)}")  # True
print(f"Type of my_car: {type(my_car)}")  # <class '__main__.Car'>


# =============================================================================
# 2. CONSTRUCTOR (__init__ method)
# =============================================================================
# The __init__ method initializes object attributes when created

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating objects with constructor
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())  # Hi, I'm Alice and I'm 25 years old.
print(person2.introduce())  # Hi, I'm Bob and I'm 30 years old.


# =============================================================================
# 3. INSTANCE vs CLASS VARIABLES
# =============================================================================

class Student:
    # Class variable - shared by all instances
    school_name = "Python Academy"
    student_count = 0
    
    def __init__(self, name, grade):
        # Instance variables - unique to each object
        self.name = name
        self.grade = grade
        Student.student_count += 1  # Accessing class variable
    
    def display(self):
        return f"{self.name} studies at {Student.school_name} in grade {self.grade}"

s1 = Student("John", "A")
s2 = Student("Emma", "B")

print(f"Total students: {Student.student_count}")  # 2
print(s1.display())  # John studies at Python Academy in grade A


# =============================================================================
# 4. TYPES OF METHODS
# =============================================================================

class Calculator:
    pi = 3.14159  # Class variable
    
    def __init__(self, value):
        self.value = value  # Instance variable
    
    # Instance Method - accesses instance data via 'self'
    def square(self):
        return self.value ** 2
    
    # Class Method - accesses class data via 'cls'
    @classmethod
    def get_pi(cls):
        return cls.pi
    
    # Static Method - doesn't access instance or class data
    @staticmethod
    def add(a, b):
        return a + b

calc = Calculator(5)
print(f"Square: {calc.square()}")       # 25 (Instance method)
print(f"Pi: {Calculator.get_pi()}")     # 3.14159 (Class method)
print(f"Add: {Calculator.add(3, 4)}")   # 7 (Static method)


# =============================================================================
# 5. INHERITANCE
# =============================================================================
# Child class inherits attributes and methods from parent class

# Parent/Base Class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child/Derived Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Method overriding
        return "Woof! Woof!"
    
    def fetch(self):  # New method in child class
        return f"{self.name} is fetching the ball!"

# Child Class
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")
    
    def make_sound(self):
        return "Meow!"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.info())        # Buddy is a Dog
print(dog.make_sound())  # Woof! Woof!
print(dog.fetch())       # Buddy is fetching the ball!
print(cat.make_sound())  # Meow!


# =============================================================================
# 6. MULTIPLE INHERITANCE
# =============================================================================

class Father:
    def skills(self):
        return "Programming, Driving"

class Mother:
    def skills(self):
        return "Cooking, Painting"
    
    def hobby(self):
        return "Reading"

# Child inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        return f"Father's skills: {Father.skills(self)}, Mother's skills: {Mother.skills(self)}"

child = Child()
print(child.skills())  # Father's skills: Programming, Driving, Mother's skills: Cooking, Painting
print(child.hobby())   # Reading (inherited from Mother)


# =============================================================================
# 7. POLYMORPHISM
# =============================================================================
# Same method name behaves differently for different classes

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Polymorphism in action - same method, different behavior
shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 4)]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area()}")


# =============================================================================
# 8. ENCAPSULATION
# =============================================================================
# Bundling data and methods, restricting direct access to some components

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self._account_type = "Savings"  # Protected (convention: single underscore)
        self.__balance = balance    # Private (name mangling: double underscore)
    
    # Getter method
    def get_balance(self):
        return self.__balance
    
    # Setter method with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount!"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. Remaining: ${self.__balance}"
        return "Insufficient funds or invalid amount!"

account = BankAccount("Alice", 1000)
print(account.owner)          # Alice (Public - accessible)
print(account._account_type)  # Savings (Protected - accessible but not recommended)
# print(account.__balance)    # Error! Private - not directly accessible
print(account.get_balance())  # 1000 (Access via getter)
print(account.deposit(500))   # Deposited $500. New balance: $1500


# =============================================================================
# 9. ABSTRACTION
# =============================================================================
# Hiding complex implementation details, showing only essential features

from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Must be implemented by child classes
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):  # Concrete method
        return "I am a shape"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

# shape = Shape()  # Error! Cannot instantiate abstract class
square = Square(5)
print(f"Square Area: {square.area()}")           # 25
print(f"Square Perimeter: {square.perimeter()}")  # 20
print(square.description())  # I am a shape


# =============================================================================
# 10. SPECIAL/MAGIC/DUNDER METHODS
# =============================================================================

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation for users
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # String representation for developers
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Length
    def __len__(self):
        return self.pages
    
    # Comparison
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # Addition (combine books)
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Python Basics", "John Doe", 200)
book2 = Book("Advanced Python", "Jane Smith", 350)

print(str(book1))           # 'Python Basics' by John Doe
print(repr(book1))          # Book('Python Basics', 'John Doe', 200)
print(f"Pages: {len(book1)}")  # Pages: 200
print(f"Total pages: {book1 + book2}")  # Total pages: 550


# =============================================================================
# 11. PROPERTY DECORATORS (Getters & Setters)
# =============================================================================

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Getter for fahrenheit (calculated)"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit"""
        self.celsius = (value - 32) * 5/9  # Uses celsius setter for validation

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")       # 25°C
print(f"Fahrenheit: {temp.fahrenheit}°F")  # 77.0°F

temp.fahrenheit = 100  # Set using fahrenheit
print(f"Celsius: {temp.celsius}°C")  # 37.77...°C


# =============================================================================
# 12. COMPOSITION (Has-A Relationship)
# =============================================================================
# Building complex objects from simpler ones

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started!"

class Wheel:
    def __init__(self, size):
        self.size = size

class CarComposition:
    def __init__(self, brand, engine_hp, wheel_size):
        self.brand = brand
        self.engine = Engine(engine_hp)  # Has-A Engine
        self.wheels = [Wheel(wheel_size) for _ in range(4)]  # Has-A Wheels
    
    def start_car(self):
        return f"{self.brand}: {self.engine.start()}"

my_car = CarComposition("Tesla", 400, 18)
print(my_car.start_car())  # Tesla: Engine started!
print(f"Engine Power: {my_car.engine.horsepower} HP")  # 400 HP
print(f"Number of wheels: {len(my_car.wheels)}")  # 4


# =============================================================================
# SUMMARY OF OOP CONCEPTS
# =============================================================================
"""
1. CLASS: Blueprint for creating objects
2. OBJECT: Instance of a class
3. CONSTRUCTOR (__init__): Initializes object attributes
4. INSTANCE VARIABLES: Unique to each object
5. CLASS VARIABLES: Shared by all instances
6. METHODS: Instance, Class (@classmethod), Static (@staticmethod)
7. INHERITANCE: Child class inherits from parent class
8. POLYMORPHISM: Same method behaves differently for different classes
9. ENCAPSULATION: Bundling data + methods, restricting access (public, _protected, __private)
10. ABSTRACTION: Hiding complexity using abstract classes
11. MAGIC METHODS: __str__, __repr__, __len__, __eq__, __add__, etc.
12. PROPERTIES: @property decorator for controlled access to attributes
13. COMPOSITION: Building objects from other objects (Has-A relationship)
"""

print("\n✅ OOP Concepts file created successfully!")
