"""
Name :Nrushanth Suthaharan
Description: S1 2017 CCC
"""

n = int(input())

swifts = input()
semas = input()

swifts = swifts.split()
swifts = [eval(i) for i in swifts]

semas = semas.split()
semas = [eval(i) for i in semas]

sum_swift = sum(swifts)
sum_sema = sum(semas)
day =n
for i in range(n-1,-1,-1):

  if (sum_swift == sum_sema):
    
    break
  
  sum_swift -= swifts[i]
  sum_sema -= semas[i]
  day -= 1

print(day)

"""
3
1 3 3
2 2 6

3
1 2 3
4 5 6

4
1 2 3 4
1 3 2 4
"""