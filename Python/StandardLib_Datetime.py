"""
StandardLib_Datetime.py
A comprehensive guide to working with dates and times in Python using the `datetime` module.
"""

import datetime
from datetime import date, time, timedelta

def main():
    print("--- 1. Current Date and Time ---")
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now}")
    
    today = datetime.date.today()
    print(f"Today's Date: {today}")
    
    print("\n--- 2. Creating Date and Time Objects ---")
    custom_date = date(2025, 12, 25)
    print(f"Custom Date (Christmas 2025): {custom_date}")
    
    custom_time = time(14, 30, 0)
    print(f"Custom Time (2:30 PM): {custom_time}")
    
    custom_datetime = datetime.datetime(2025, 12, 25, 14, 30, 0)
    print(f"Custom Datetime: {custom_datetime}")

    print("\n--- 3. Formatting Dates (strftime) ---")
    # strftime = string format time
    print(f"Formatted Date: {now.strftime('%A, %B %d, %Y')}")
    print(f"Formatted Time: {now.strftime('%I:%M %p')}")
    
    print("\n--- 4. Parsing Strings into Dates (strptime) ---")
    # strptime = string parse time
    date_string = "21 June, 2026"
    parsed_date = datetime.datetime.strptime(date_string, "%d %B, %Y")
    print(f"Parsed Date from string '{date_string}': {parsed_date.date()}")

    print("\n--- 5. Timedeltas (Date Math) ---")
    # Adding or subtracting time
    future_date = now + timedelta(days=10, hours=5)
    print(f"Date 10 days and 5 hours from now: {future_date}")
    
    past_date = now - timedelta(weeks=2)
    print(f"Date 2 weeks ago: {past_date}")
    
    # Difference between two dates
    bday = datetime.datetime(now.year + 1, 1, 1)
    time_to_bday = bday - now
    print(f"Time until New Year: {time_to_bday.days} days")

if __name__ == "__main__":
    main()
