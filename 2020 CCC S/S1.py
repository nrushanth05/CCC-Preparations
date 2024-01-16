"""
Name: Nrushanth Suthaharan
Description: S1 2020 CCC
"""

n = int(input())
lines = []
speeds = []
for i in range(n):
  line = [int(x) for x in input().split()]
  lines.append(line)
lines = sorted(lines)
#print(lines)
for i in range(1,n):
  time_diff = lines[i][0]-lines[i-1][0]
  pos_diff = lines[i][1]-lines[i-1][1]
  speed = abs(pos_diff/time_diff)
  speeds.append(speed)

#print(speeds)

print(max(speeds))

"""



3
0 100
20 50
10 120

5
20 -5
0 -17
10 31
5 -3
30 11
"""