csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
friends_list = ' '.join(
    ' '.join(' '.join(csv.split(',')).split(':')).split(';')).split()

friends_list_2 = csv.replace(';', ',').replace(':', ',').split(',')
print(friends_list)
print(friends_list_2)
