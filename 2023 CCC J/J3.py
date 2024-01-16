day1 = 0
day2 = 0
day3 = 0
day4 = 0
day5 = 0

n = int(input())

for i in range(n):
  current = input().split()
  for i in range(len(current)):
    if i == 0 and current[i] == "Y":
      day1 += 1
    elif i ==1 and current[i] == "Y":
      day2 += 1
    elif i==2 and current[i] == "Y":
      day3 += 1
    elif i== 3 and current[i] == "Y":
      day4 += 1
    elif i == 4 and current[i] == "Y":
      day5 += 1

list = [day1,day2,day3,day4,day5]
max = max(list)
output = ""
for i in range(len(list)):
  if list[i] == max:
    output += str(i+1) + ", "
print(output[:-2])
"""
3
Y Y Y
Y . Y
Y Y Y

7
Y . Y . Y
Y Y Y Y Y
Y . . Y .
. Y . . Y
. . Y . Y
Y Y Y . .
. . . Y .
"""