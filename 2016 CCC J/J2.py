"""
Name: Nrushanth Suthaharan
Date: Nov 24, 2022
Description: J2 2016, CCC
"""


square = []
for i in range(4):
  row = input().split()
  #print(row)
  square.append(row)

#print(square)
sum_row = 0;
sum_col = 0;
list_sum = []
for i in range(4):
  for j in range(4):
    sum_row += int (square[i][j])
    sum_col += int (square[j][i])
  list_sum.append(sum_row)
  sum_row =0
  list_sum.append(sum_col)
  sum_col = 0
count = 0
#print(list_sum)
for i in range(1,len(list_sum)-1):
  if list_sum[i] == list_sum[i-1]:
    count += 1
#print(count)
#print(len(list_sum))
if count == len(list_sum)-2:
  print("magic")
else:
  print("not magic")

"""
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1

5 10 1 3
10 4 2 3
1 2 8 5
3 3 5 0
"""
  
    

  

