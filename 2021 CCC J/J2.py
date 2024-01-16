n = int(input())

names = []
numbers = []
for i in range(n):
  name = input()
  names.append(name)

  number = int(input())
  numbers.append(number)

highest_bid = max(numbers)

name_index = numbers.index(highest_bid)
name = names[name_index]
print(name)

"""
3
Ahmed
300
Suzanne
500
Ivona
450

2
Ijeoma
20
Goor
20
"""

  
  