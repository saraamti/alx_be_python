# Prompt the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using Match Case (Python 3.10+)
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority level."

# Modify the message based on whether the task is time-bound or not
if time_bound == "yes":
    # Use 'Reminder' if time-bound
    print(f"Reminder: {reminder} This task requires immediate attention today!")
else:
    # Use 'Note' if not time-bound
    print(f"Note: {reminder} Consider completing it when you have free time.")
