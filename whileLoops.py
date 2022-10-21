# i = 0
# while i < 5:
#     i += 1
#     print(f'{i}.{"*"*i}Loops are awesome{"*"*i}')


# The guessing game exercise

number = 67
guesses = 0
max_guesses = 5
userInput = 0

while guesses < max_guesses:
    userInput = int(input('guess a number: '))
    guesses += 1
    if userInput > number:
        print('too high, try again')
    elif userInput < number:
        print('too low,try again')
    elif userInput == number:
        print(f'you guessed the correct number, {userInput}')
        break
if userInput != number:
    print('your guesses are over, get them next time')
