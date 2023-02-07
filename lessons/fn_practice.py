"""Example functions to learn definition and calling sytax"""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of 2 values"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    
max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print(other_max_number)