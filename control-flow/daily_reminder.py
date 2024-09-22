# Prompt the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using Match Case (Python 3.10+)
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Output the customized reminder
print(reminder)
