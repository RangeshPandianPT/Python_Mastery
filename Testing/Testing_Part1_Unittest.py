"""
Testing_Part1_Unittest.py
An introduction to unit testing in Python using the built-in `unittest` framework.
"""

import unittest

# --- Functions to Test ---
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class StringManipulator:
    def reverse_string(self, s):
        return s[::-1]

    def capitalize_words(self, s):
        return s.title()

# --- Test Cases ---
# Test classes must inherit from unittest.TestCase
class TestMathOperations(unittest.TestCase):
    
    # Test methods must start with 'test_'
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(10, 3), 3.3333333, places=6)
        
        # Testing for exceptions
        with self.assertRaises(ValueError):
            divide(10, 0)

class TestStringManipulator(unittest.TestCase):
    
    # setUp runs BEFORE every test method
    def setUp(self):
        self.manipulator = StringManipulator()
        
    def test_reverse_string(self):
        result = self.manipulator.reverse_string("hello")
        self.assertEqual(result, "olleh")
        
    def test_capitalize_words(self):
        result = self.manipulator.capitalize_words("python mastery guide")
        self.assertEqual(result, "Python Mastery Guide")

if __name__ == "__main__":
    # Runs all tests in the script
    print("Running Unittests...")
    unittest.main(verbosity=2)
