from datetime import datetime, date

def get_days_from_today(date_str):
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        today = date.today()

        total_days = (today - input_date).days

        return total_days
    except ValueError:
        return "Wrong format of date. Use YYYY-MM-DD"

user_input_date = input("Enter date YYYY-MM-DD:")
print("Amount of days", get_days_from_today(user_input_date))