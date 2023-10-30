#import calc module
import calculator


#2 input numbers
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

operation = str(input("What function will you use(add, subtract, multiply, divide): "))

#if statements to know which function to use
if operation == 'add':
    outcome = calculator.add(num1, num2)
    print(outcome)
elif operation == 'subtract':
    outcome = calculator.subtract(num1, num2)
    print(outcome)
elif operation == 'multiply':
    outcome = calculator.multiply(num1, num2)
    print(outcome)
elif operation == 'divide':
    outcome = calculator.divide(num1, num2)
    print(outcome)

