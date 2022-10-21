def greeting(name, age=23):
    print(f'Hello {name} your age is {age}!')


greeting('Gislain')


def greeting2(name, color='red', age=28):
    print(f'Hello {name.capitalize()}, you are {int(age)+1}!')
    print(f'we hear you like the color {color.lower()}!')


name = input('what is your name?: ')
age = input('what is your age?: ')
color = input('Favorite color is: ')

greeting2(name, color, age)
