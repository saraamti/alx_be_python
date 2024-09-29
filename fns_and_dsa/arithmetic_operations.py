def perform_operation (num1, num2, operation):
    """
    Perform basic arithmetic operations based on the input.
    
    :param num1: First number (float)
    :param num2: Second number (float)
    :param operation: A string representing the operation ('add', 'subtract', 'multiply', 'divide')
    :return: Result of the operation or a message if division by zero occurs
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"
    
