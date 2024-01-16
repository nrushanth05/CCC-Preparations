"""
Name: Nrushanth Suthaharan
Date: May 9, 2022
Description: J5 2022 CCC
"""

n = int(input())


t = int(input())

pool = []
for i in range(n):
  r = []
  for j in range(n):
    r.append(" ")
  pool.append(r)
#print(pool)
#print("\n\n\n\n\n\n")



for i in range(t):
  tree = input()
  row = int(tree[:tree.find(" ")])
  col= int(tree[tree.find(" ")+1:])
  
  pool[row-1][col-1] = "t"
"""

for i in range(len(list_t)):
  current_tree = list_t[i]
  row = int(current_tree[:current_tree.find(" ")])
  column = int(current_tree[current_tree.find(" ")+1:])
  pool[row-1][column-1] = "t"
"""
print(pool)

# function to check if t is in row
def if_in_column(x):
  for i in range(n):
    current_list = pool[i]
    if "t" in current_list[x-1]:
      return True
#function to check if t is in column

def if_in_row(y):
  if "t" in pool[n-y-1]:
    return True
# coding to analyze pool

squares = []

# find possible square
def find_squares():
  currentx_initial = 0
  currenty_initial = 0
  currentx = 0
  currenty = 0
  for i in range(n):
    if if_in_row(currenty) == True:
      squares.append(currenty-currenty_initial)
      currenty += 2
      currenty_initial = currenty
    else:
      currenty += 1  
    if if_in_column(currentx) == True:
      squares.append(currentx-currentx_initial)
      currentx += 2
      currentx_initial = currentx
    else:
      currentx += 1
      
    
  squares.append(currentx)
find_squares()
print(squares)

    
#test codes
"""
15
8
4 7
4 1
14 11
10 6
13 4
4 10
10 3
9 14
"""

