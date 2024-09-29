from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the date in "YYYY-MM-DD HH:MM:SS" format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a future date
def calculate_future_date(current_date):
    # Prompt the user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        # Print the future date in "YYYY-MM-DD" format
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Please enter a valid number of days.")

if __name__ == "__main__":
    # Display the current date and time
    current_date = display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date(current_date)
