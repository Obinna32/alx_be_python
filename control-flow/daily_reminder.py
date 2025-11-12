prioity_variable = input("Enter your task: ")
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

