"""
Name: Nrushanth Suthaharan
Description: 2016 S3 CCC
"""

line1 = input()

n = int(line1.split()[0])

m = int(line1.split()[1])

line2 = input()

phos = line2.split()
phos = [eval(i) for i in phos]

roads = []

for i in range(n-1):
  current = input()
  road = current.split()
  road = [eval(i) for i in road]
  #print(road)
  roads.append(road)
#print(roads)

path = 0
count = 0
start = roads[0]
while True:
  current_road = roads[count]
  if (current_road[1] in phos):
    path += 1
  
  count = current_road[1]
  
  



"""
8 2
5 2
0 1
0 2
2 3
4 3
6 1
1 5
7 3
"""