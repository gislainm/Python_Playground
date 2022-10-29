names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

newName = input('Enter the first new name: ')
new_name2 = input('Enter the second new name: ')

names.append(newName)
names1.append(new_name2)

for name in  names:
    names = name.split()
    if len(names) == 2:
        print(f'{names[0].capitalize()} {names[1].capitalize()}! You are invited to the party on saturday. ')
    else:
      print(f'{names[0].capitalize()}! You are invited to the party on saturday. ')  

for name in names1:
    names = name.split()
    if len(names) == 2:
        print(f'{names[0].capitalize()} {names[1].capitalize()}! You are invited to the party on saturday. ')
    else:
        print(f'{names[0].capitalize()}! You are invited to the party on saturday. ')