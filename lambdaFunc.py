def square(x):
    return x*x


def square1(x): return x*x


print(square1(2))


f = lambda x:x+5

print(f(2))

strip_spaces = lambda str:''.join(str.split())

print(strip_spaces('Gislain is a  good man'))

list_a = [1,2,3,4]
list_b = [3,4,5,6,7]

join_list_no_duplicates = lambda list_a,list_b:list(set(list_a+list_b))

print(join_list_no_duplicates(list_a ,list_b ))

def create_quad_func(a,b,c):
    '''return function f(x) = ax^2 + bx + c'''
    return lambda x:a*x**2+b*x+c
f1 = create_quad_func(2,4,6)
# g = 
print(f1(2))
# print(g(2))

signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # Lexicographic sort
#write sorting by integer
print(sorted(signups,key=lambda str:int(str[3:])) )# Integer sort


class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]


#Exercise: Sort this by score using lambda!
#write code here
player_list.sort(key=lambda player:player.score,reverse = True)
print([player.name for player in player_list])