# Exception Handling in Python

print("--- Basic Try-Except ---")
try:
    # Attempting to divide by zero
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("\n--- Multiple Except Blocks ---")
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid integer conversion!")
except TypeError:
    print("Error: Type mismatch!")

print("\n--- Try-Except-Else ---")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    # Executes if no exception occurs
    print(f"Division successful. Result is {result}")

print("\n--- Try-Except-Finally ---")
try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Error: File not found!")
finally:
    # Executes regardless of an exception
    print("Execution of try-except block finished.")

print("\n--- Raising Exceptions ---")
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age is {age}")

try:
    check_age(-5)
except ValueError as e:
    print(f"Caught an exception: {e}")
