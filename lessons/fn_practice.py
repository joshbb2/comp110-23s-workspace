"""Example functions to learn definition and calling sytax"""

x: int = 1
y: int = 10

def my_max(num1: int, num2: int) -> int:
    """Returns the maximum value out of 2 values"""
    if num1 >= num2:
        return num1 + 0
    else: #number1 < number2
        return num2
    
max_number: int = my_max(1,10)

