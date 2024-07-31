# perform simple calculator by using arithmatic operator 

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Raises ValueError if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_float(prompt):
    """Prompt the user for a float input and handle invalid inputs."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    """Prompt the user for an arithmetic operation."""
    operations = {
        '1': 'Add',
        '2': 'Subtract',
        '3': 'Multiply',
        '4': 'Divide'
    }
    
    print("Select an operation:")
    for key, value in operations.items():
        print(f"{key}: {value}")
        
    while True:
        choice = input("Enter the number corresponding to the operation: ")
        if choice in operations:
            return choice
        else:
            print("Invalid choice. Please select a valid operation.")

def main():
    print("Welcome to the Simple Calculator!")
    
    # Get user input for the first number
    num1 = get_float("Enter the first number: ")
    
    # Get user input for the second number
    num2 = get_float("Enter the second number: ")
    
    # Get user choice of operation
    operation = get_operation()
    
    # Perform the operation based on user choice
    if operation == '1':
        result = add(num1, num2)
        op_symbol = '+'
    elif operation == '2':
        result = subtract(num1, num2)
        op_symbol = '-'
    elif operation == '3':
        result = multiply(num1, num2)
        op_symbol = '*'
    elif operation == '4':
        try:
            result = divide(num1, num2)
            op_symbol = '/'
        except ValueError as e:
            print(e)
            return
    
    # Display the result
    print(f"The result of {num1} {op_symbol} {num2} = {result}")
    
if __name__ == "__main__":
    main()

