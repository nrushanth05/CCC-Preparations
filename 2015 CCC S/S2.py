"""
Name: Nrushanth Suthaharan
Date: Feb 9, 2023
Description: 2015 CCC S2
"""


j = int(input())
a = int(input())

list_j = []
count = 0
for i in range(1,j+1):
  list_j.append(input() + " " + str(i))
#print(list_j)
for i in range(a):
  current = input()
  if current in list_j:
    list_j.pop(list_j.index(current))
    count += 1
  elif current[0] == "S" and ("M "+ current[2:]) in list_j:
    list_j.pop(list_j.index("M " + current[2:]))
    count +=1 
  elif current[0] == "S" and  ("L " + current[2:]) in list_j:
    list_j.pop(list_j.index("L " + current[2:]))
    count += 1
  elif current[0] == "M" and ("L " + current[2: ]) in list_j:
    list_j.pop(list_j.index("L " + current[2:]))
    count += 1
#print(list_j)
print(count)

"""
4
3
M
S
S
L
L 3
S 3
L 1

################
5
2
S
L
M
M
S
M 3
S 4
"""
    