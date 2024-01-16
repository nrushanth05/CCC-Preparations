"""
Name: Nrushanth Suthaharan
Description: This program will ask the user for a number and then print out the multiplication table for that number.
"""
x = int(input())

list_pair_x = []
for i in range(x):
  pair = input()
  
  list_pair_x.append(pair)

y = int(input())

list_pair_y = []
for i in range(y):
  pair = input()
  
  list_pair_y.append(pair)

g = int(input())

list_groups = []
for i in range(g):
  group = input()
  #ind = group.split()
  list_groups.append(group)

def check_if_together(a,b):
  for i in range(len(list_groups)):
    current_group = list_groups[i]
    #print(current_group)
    if str(a) in current_group and str(b) in current_group:
      return True

def check_if_apart(a,b):
  for i in range(len(list_groups)):
    current_group = list_groups[i]
    #print(current_group)
    if str(a) in current_group and str(b) not in current_group or str(a) not in current_group and str(b) in current_group:
      return True 
    

constraint_num = 0
#check first constraints
for i in range(x):
  current_x = list_pair_x[i]
  current = current_x.split()
  if check_if_apart(current[0],current[1]):
    constraint_num += 1

for i in range(y):
  current_y = list_pair_y[i]
  current = current_y.split()
  if check_if_together(current[0],current[1]):
    constraint_num += 1

print(constraint_num)

"""
1
ELODIE CHI
0
2
DWAYNE BEN ANJALI
CHI FRANCOIS ELODIE

3
A B
G L
J K
2
D F
D G
4
A C G
B D F
E H I
J K L

"""