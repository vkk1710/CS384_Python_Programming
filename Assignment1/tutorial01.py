# Function to add two numbers
def add(num1, num2):
    if (isinstance(num1, str) or isinstance(num2, str)):
        return 0
    addition = num1 + num2
    return addition


# Function to subtract two numbers
def subtract(num1, num2):
    if (isinstance(num1, str) or isinstance(num2, str)):
        return 0
    subtraction = num1 - num2
    return subtraction


# Function to multiply two numbers
def multiply(num1, num2):
    #Multiplication Logic
    if (isinstance(num1, str) or isinstance(num2, str)):
        return 0
    multiplication = num1 * num2
    return multiplication


# Function to divide two numbers
def divide(num1, num2):
    #DivisionLogic
    if (num2 == 0 or isinstance(num1, str) or isinstance(num2, str)):
        return 0
    division = num1 / num2
    return division
