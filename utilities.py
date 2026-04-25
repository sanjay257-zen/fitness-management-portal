from datetime import datetime


def format_date(date_obj):
    """Formats a date object to a string format YYYY-MM-DD"""
    return date_obj.strftime('%Y-%m-%d')


def validate_date(date_str):
    """Validates if a date string is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def days_between(start_date, end_date):
    """Calculates the number of days between two date strings in YYYY-MM-DD format."""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    return (end - start).days
