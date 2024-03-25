from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Prepare data structure to store birthdays by weekday
    birthdays = defaultdict(list)
    today = datetime.today().date()
    one_week_ahead = today + timedelta(days=7)

    for user in users:
        name = user["name"]
        # Convert birthday to this year's date
        birthday_this_year = user["birthday"].date().replace(year=today.year)
        # If birthday has already passed this year, consider next year's date
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        # Calculate the delta days from today
        delta_days = (birthday_this_year - today).days

        # If the birthday falls within the next week
        if 0 <= delta_days <= 7:
            # Convert weekend birthdays to Monday
            if birthday_this_year.weekday() >= 5:  # 5 for Saturday, 6 for Sunday
                day_to_congratulate = "Monday"
            else:
                day_to_congratulate = birthday_this_year.strftime('%A')
            birthdays[day_to_congratulate].append(name)

    # Display result
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

    # Example usage:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 12)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 26)},
    {"name": "Jan Koum", "birthday": datetime(1976, 3, 24)},
]
print(get_birthdays_per_week(users))