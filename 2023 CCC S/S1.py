c = int(input())

lane1 = [int(x) for x in input().split()]

lane2 = [int(x) for x in input().split()]
#print(lane1)
#print(lane2)
sum = 3*(sum(lane1)+sum(lane2))
#print(sum)
if(c==1):
  if(lane1[0] == 1 and lane2[0]==1):
    sum-=2
else:
  for i in range(c-1):
    current1 = lane1[i]
    current2 = lane2[i]
    #print(current1)
    #print(current2)
    if(i%2 == 0):
      if(current1 == 1 and lane1[i+1] ==1):
        sum -= 2
      if(current1 == 1 and current2 == 1):
        sum -= 2
      if(current2 == 1 and lane2[i+1] ==1):
        sum -= 2
    else:
      if(current1 == 1 and lane1[i+1] == 1):
        sum -= 2
      if(current2 == 1 and lane2[i+1]==1):
        sum -= 2
      if(i == c-2 and lane1[-1] ==1 and lane2[-1] == 1):
        sum-=2
  
#print(lane1)
#print(lane2)
print(sum)

"""
5
1 0 1 0 1
0 0 0 0 0

7
0 0 1 1 0 1 0
0 0 1 0 1 0 0

9
0 1 0 0 1 1 1 0 0
0 0 0 0 1 0 1 0 1

7
1 1 1 1 1 1 1
1 1 1 1 1 1 1

3
1 1 1
1 1 1

3
1 1 0
1 1 0

4
0 1 0 1
0 1 0 1
"""