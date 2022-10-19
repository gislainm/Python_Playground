my_numbers = [1, 2, 3, 4, 5, 6]

print(len(my_numbers))
for i in my_numbers:
    print(my_numbers.index(i))
print(my_numbers)
my_numbers.reverse()
print(max(my_numbers))

my_numbers.append(7)
my_numbers.insert(0, 0)
my_numbers.remove(0)
print(my_numbers)
