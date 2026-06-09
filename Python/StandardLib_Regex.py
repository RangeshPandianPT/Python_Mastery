"""
StandardLib_Regex.py
A guide to using Regular Expressions in Python using the `re` module.
"""

import re

def main():
    text = "Hello! My email is python_mastery@example.com and my phone number is 123-456-7890. Please contact me before 2026-12-31."

    print(f"Original Text: {text}\n")

    print("--- 1. re.search (Find first match) ---")
    # Searching for a phone number pattern
    phone_pattern = r"\d{3}-\d{3}-\d{4}"
    match = re.search(phone_pattern, text)
    if match:
        print(f"Found phone number: {match.group()}")

    print("\n--- 2. re.findall (Find all matches) ---")
    # Extracting all numbers
    numbers = re.findall(r"\d+", text)
    print(f"All numbers found: {numbers}")

    print("\n--- 3. Extracting Emails ---")
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    print(f"Found emails: {emails}")

    print("\n--- 4. re.sub (Search and Replace) ---")
    # Redact the phone number
    redacted_text = re.sub(phone_pattern, "[REDACTED]", text)
    print(f"Redacted Text: {redacted_text}")

    print("\n--- 5. re.split (Split by pattern) ---")
    # Split text by spaces or punctuation
    words = re.split(r"[\s.!]+", text)
    # Remove empty strings from list
    words = [w for w in words if w] 
    print(f"Words extracted: {words[:5]}...")

    print("\n--- 6. Using Match Groups ---")
    date_pattern = r"(\d{4})-(\d{2})-(\d{2})"
    date_match = re.search(date_pattern, text)
    if date_match:
        print(f"Full Date found: {date_match.group(0)}")
        print(f"Year: {date_match.group(1)}")
        print(f"Month: {date_match.group(2)}")
        print(f"Day: {date_match.group(3)}")

if __name__ == "__main__":
    main()
