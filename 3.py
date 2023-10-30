# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")


#my functions
def add():
    outcome = first_number + second_number
    return outcome
def subtract():
    outcome = first_number - second_number
    return outcome
def multiply():
    outcome = first_number * second_number
    return outcome
def divide():
    outcome = first_number / second_number
    return outcome


# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

operations = input("Would you like to add/subtract/multiple/divide: ")
if operations == 'add':
    print(add())
elif operations == 'subtract':
    print(subtract())
elif operations == 'multiply':
    print(multiply())
elif operations == 'divide':
    print(divide())


