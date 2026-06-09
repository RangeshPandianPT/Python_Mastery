# File Handling in Python

# 1. Opening and Reading a File
# Creating a dummy file first
with open('sample_text.txt', 'w') as file:
    file.write("Hello, World!\nWelcome to File Handling in Python.\nThis is a sample text file.")

# Reading the file
print("--- Reading File ---")
with open('sample_text.txt', 'r') as file:
    content = file.read()
    print(content)

# 2. Reading line by line
print("\n--- Reading Line by Line ---")
with open('sample_text.txt', 'r') as file:
    for line in file:
        print(line.strip()) # strip() removes the newline character

# 3. Appending to a file
print("\n--- Appending to File ---")
with open('sample_text.txt', 'a') as file:
    file.write("\nAppending a new line to the file.")

# Check the appended content
with open('sample_text.txt', 'r') as file:
    print(file.read())

# 4. Writing multiple lines
print("\n--- Writing Multiple Lines ---")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('multiple_lines.txt', 'w') as file:
    file.writelines(lines)

with open('multiple_lines.txt', 'r') as file:
    print(file.read())
