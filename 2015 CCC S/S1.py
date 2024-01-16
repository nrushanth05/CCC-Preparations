"""
Name: Nrushanth Suthaharan
Date: Feb 9, 2023
Description: S1 2015, CCC
"""

n = int(input())
list = []

for i in range(n):
  current = int(input())
  if (current == 0):
    list.pop()
  else:
    list.append(current)


print(sum(list))

"""
10
1
3
5
4
0
0
7
0
0
6
"""