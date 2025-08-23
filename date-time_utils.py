"""
date_time_utils.py

Demonstrates working with date and time in Python:
1. Getting current date/time
2. Formatting dates
3. Parsing strings into datetime objects
4. Date arithmetic
5. Time zone handling

Includes:
- Exception handling
- Reusable functions
"""

from datetime import datetime, timedelta
import pytz  # Install with: pip install pytz

# ---------------------------
# Current Date and Time
# ---------------------------

def get_current_datetime(timezone_str="UTC"):
    """Returns the current date and time in the given timezone."""
    try:
        tz = pytz.timezone(timezone_str)
        now = datetime.now(tz)
        print(f"📅 Current Date & Time in {timezone_str}: {now}")
        return now
    except pytz.UnknownTimeZoneError:
        print(f"❌ Unknown timezone: {timezone_str}")

# ---------------------------
# Formatting Dates
# ---------------------------

def format_datetime(dt, format_str="%Y-%m-%d %H:%M:%S"):
    """Formats a datetime object into a string."""
    try:
        formatted = dt.strftime(format_str)
        print(f"📝 Formatted DateTime: {formatted}")
        return formatted
    except Exception as e:
        print(f"❌ Error formatting datetime: {e}")

# ---------------------------
# Parsing Strings into Dates
# ---------------------------

def parse_datetime(date_str, format_str="%Y-%m-%d %H:%M:%S"):
    """Parses a string into a datetime object."""
    try:
        dt = datetime.strptime(date_str, format_str)
        print(f"📥 Parsed DateTime: {dt}")
        return dt
    except ValueError as e:
        print(f"❌ Error parsing date string: {e}")

# ---------------------------
# Date Arithmetic
# ---------------------------

def add_days(dt, days):
    """Adds or subtracts days from a datetime object."""
    try:
        new_date = dt + timedelta(days=days)
        print(f"📆 New Date after {days} days: {new_date}")
        return new_date
    except Exception as e:
        print(f"❌ Error adding days: {e}")

# ---------------------------
# Example Usage
# ---------------------------

if __name__ == "__main__":
    # 1. Current date/time in IST
    now_ist = get_current_datetime("Asia/Kolkata")

    # 2. Format date/time
    format_datetime(now_ist, "%A, %d %B %Y %I:%M %p")

    # 3. Parse date string
    date_str = "2025-08-23 14:30:00"
    parsed_dt = parse_datetime(date_str)

    # 4. Add days
    add_days(parsed_dt, 7)  # 7 days later
    add_days(parsed_dt, -3) # 3 days earlier