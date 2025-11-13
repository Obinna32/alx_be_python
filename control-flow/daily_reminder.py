'''prioity_variable = input("Enter your task: ")
priority_level = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if priority_level == "high":
    if time_bound == "yes":
        print(f"Reminder: '{prioity_variable}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{prioity_variable}' is a high priority task. Consider completing it when you have free time.")
elif priority_level == "medium":
    if time_bound == "yes":
        print(f"Reminder: '{prioity_variable}' is a medium priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{prioity_variable}' is a medium priority task. Consider completing it when you have free time.")
if priority_level == "low":
    if time_bound == "yes":
        print(f"Reminder: '{prioity_variable}' is a low priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{prioity_variable}' is a low priority task. Consider completing it when you have free time.")
'''


task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

while priority not in ["high", "medium", "low"]:
    print("Invalid input. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

while time_bound not in ["yes", "no"]:
    print("Invalid input. Please enter yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unspecified priority."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

print("\nReminder: ",reminder)