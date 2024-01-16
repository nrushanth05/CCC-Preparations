"""
Name: Nrushanth Suthaharan
Description: S2 2017 CCC
"""

n = int(input())

data = input()

data = data.split()
data = [eval(i) for i in data]


highs = []
lows = []

for i in range(int(n/2+0.5)):
  high = max(data)
  low = min(data)

  if(high>low):
    highs.append(high)
    lows.append(low)

    data.remove(high)
    data.remove(low)
  else:
    lows.append(low)
#print(highs)
#print(lows)

highs.reverse()
lows.reverse()
for i in range(len(lows)):
  if (i >= len(highs)):
    print(lows[i])
    break
  print(str(lows[i]) + " " + str(highs[i]), end=" ")


"""
8
10 50 40 7 3 110 90 2

9
10 50 40 7 3 110 90 2 30


"""
  
    