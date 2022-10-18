name = input('what is your name?: ')
age = input('what is your age?: ')

print('Hello '+name+' your age is: ' + age)

number1 = input('Please enter the first number: ')
number2 = input('Please enter the second number: ')

calculator = float(number1) + float(number2)
print(calculator)


userName = input('Please enter you name: ')
distance = input('Please enter a distance in km: ')
distanceMile = float(distance)/1.609
print(f'Hi {userName.title()}! {distance}km is equivalent to {round(distanceMile,2)}')
