# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division with error handling for zero division and non-numeric inputs."""
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform the division and handle division by zero
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
