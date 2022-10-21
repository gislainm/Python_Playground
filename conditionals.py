from ast import operator


def degree_converter():
    c_degree = int(input('Please enter a celcius degree: '))
    return (c_degree*9/5)+32


def calculator():
    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))
    operator = input('Please enter an operator: ')
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 + num2
    elif operator == '*':
        return num1 * num2


first_input = input('Enter 1 for calculator or 2 for degree conversion: ')
if first_input == '1':
    print(calculator())
elif first_input == '2':
    print(degree_converter())
else:
    print('Invalid input')
