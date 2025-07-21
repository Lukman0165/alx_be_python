# daily_reminder.py
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Please address it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task with a deadline. Try to complete it today.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Schedule time for it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task, but has a time constraint. Complete when possible.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please use high/medium/low.")
