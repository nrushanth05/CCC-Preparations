c = int(input())
mountains = [int(x) for x in input().split()]

def get_asym( list):
  sum = 0
  count = len(list)-1
  for i in range(int(len(list)/2)):
    current = list[i]
    next = list[count]
    diff = abs(current-next)
    #print(diff)
    sum += diff
    if(i == count):
      break
    count -= 1
    

  return sum
#print(get_asym([3,1,4,1,5]))
#print(get_asym([3, 1, 4, 1, 5, 9]))
#print(get_asym([1, 4, 1, 5, 9, 2]))
def get_crop(x, list):
  y = len(list)-x+1
  main_list = []
  for i in range(y):
    current = list[i:i+x]
    main_list.append(current)

  return main_list

#print(get_crop(5,[3, 1, 4, 1, 5, 9, 2]))

final_list = []
for i in range(1,c+1):
  sum_list = []
  list_of_lists = get_crop(i,mountains)
  print(list_of_lists)
  list_symmetries = []
  for j in range(len(list_of_lists)):
    sum_list.append(sum(list_of_lists[j]))
  index = sum_list.index(min(sum_list))
  print(sum_list)
  print(index)
  print(get_asym(list_of_lists[index]))
  final_list.append(get_asym(list_of_lists[index]))

#print(final_list)
for i in range(len(final_list)):
  print(str(final_list[i]),end=" ")
    
"""
7
3 1 4 1 5 9 2

4
1 3 5 6



[1, 4, 1, 5, 9, 2]

[3, 1, 4, 1, 5, 9]
"""