"""
Name: Nrushanth Suthaharan
Date: Feb 13, 2023
Description: 2016 CCC S2
"""
dmoj = []
pend = []

question_type = int(input())
n = int(input())
dmoj_string = input()
pend_string = input()

dmoj = dmoj_string.split()
pend = pend_string.split()

dmoj = [eval(i) for i in dmoj]
pend = [eval(i) for i in pend]

dmoj2 = dmoj
pend2 = pend

sum = 0
if(question_type == 1):
  for i in range(n):
    #print(dmoj)
    #print(pend)
    #min_dmoj = min(dmoj)
    max_dmoj = max(dmoj)

    #min_pend = min(pend)
    max_pend = max(pend)

    if max_dmoj > max_pend:
      sum += max_dmoj
    else:
      sum += max_pend

    dmoj.remove(max_dmoj)
    pend.remove(max_pend)
else:
  for i in range(n):
    max_dmoj = max(dmoj2)

    min_pend = min(pend2)

    if (max_dmoj>min_pend):
      sum += max_dmoj
    else:
      sum += min_pend

    dmoj2.remove(max_dmoj)
    pend2.remove(min_pend)
print(sum)

"""
1
3
5 1 4
6 2 4

2
3
5 1 4
6 2 4

2
5
202 177 189 589 102
17 78 1 496 540
"""
