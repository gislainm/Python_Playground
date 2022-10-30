from typing import List


nums = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']
names = ['John', 'Eric', 'Michael', 'Graham', 'Joe']

comb_list = nums
comb_list.extend(letters)
comb_list.extend(names)

print(comb_list)
