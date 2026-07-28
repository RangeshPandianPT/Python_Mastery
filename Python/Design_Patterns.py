"""
Design Patterns in Python
=========================

This module demonstrates some of the most common Gang of Four (GoF) design patterns implemented in Python.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# 1. Singleton Pattern (Creational)
# Ensures a class has only one instance and provides a global point of access.
# ---------------------------------------------------------
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection instance...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Initialize connection here
        return cls._instance

# ---------------------------------------------------------
# 2. Factory Method Pattern (Creational)
# Defines an interface for creating an object, but lets subclasses decide which class to instantiate.
# ---------------------------------------------------------
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        raise ValueError(f"Unknown animal type: {animal_type}")

# ---------------------------------------------------------
# 3. Observer Pattern (Behavioral)
# Defines a one-to-many dependency so that when one object changes state, all its dependents are notified.
# ---------------------------------------------------------
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class ConcreteObserverA(Observer):
    def update(self, message):
        print(f"Observer A received: {message}")

class ConcreteObserverB(Observer):
    def update(self, message):
        print(f"Observer B received: {message}")

# ---------------------------------------------------------
# 4. Strategy Pattern (Behavioral)
# Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
# ---------------------------------------------------------
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, amount: float) -> float:
        return amount - (amount * (self.percentage / 100))

class ShoppingCart:
    def __init__(self, strategy: DiscountStrategy):
        self._strategy = strategy
        self._items = []

    def add_item(self, price: float):
        self._items.append(price)

    def checkout(self) -> float:
        total = sum(self._items)
        return self._strategy.apply_discount(total)

# ---------------------------------------------------------
# Testing the patterns
# ---------------------------------------------------------
if __name__ == "__main__":
    print("--- Singleton ---")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Are db1 and db2 the same instance? {db1 is db2}")

    print("\n--- Factory Method ---")
    dog = AnimalFactory.get_animal("dog")
    print(f"Dog says: {dog.speak()}")

    print("\n--- Observer ---")
    subject = Subject()
    obs1 = ConcreteObserverA()
    obs2 = ConcreteObserverB()
    subject.attach(obs1)
    subject.attach(obs2)
    subject.notify("State changed!")

    print("\n--- Strategy ---")
    cart = ShoppingCart(PercentageDiscount(20)) # 20% off
    cart.add_item(100)
    cart.add_item(50)
    print(f"Total after 20% discount: ${cart.checkout()}")
