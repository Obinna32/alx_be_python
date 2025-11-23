from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_form = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_form)


def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_form = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_form)


if __name__ == "__main__":
    display_current_datetime()
    user_days = int(input("Enter the number of days to add to the current date:"))
    calculate_future_date(user_days)
