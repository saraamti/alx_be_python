# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Ensure no extra spaces around the operator
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Ensure no extra spaces around the operator

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main function to interact with the user
def main():
    try:
        # Ask for the temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # Convert input to float for calculation

        # Ask if the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the conversion based on the unit
        if unit == "F":
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == "C":
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handle non-numeric input for temperature
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
