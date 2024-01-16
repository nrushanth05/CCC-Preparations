
order = input()

def is_good(order):
  number_L = order.count("L")
  number_M = order.count("M")
  number_S = order.count("S")

  if order[:number_L] == str("L"*number_L) and order[number_L :number_M+number_L] == str("M"*number_M) and order[number_M+number_L :number_S+number_M+number_L] == str("S"*number_S):
    return True
  else:
    return False
def swap(order,ind_1,ind_2):
  list_order = list(order)
  var_1 = order[ind_1]
  var_2 = order[ind_2]
  list_order[ind_1] = var_2
  list_order[ind_2] = var_1

  new_order = "".join(list_order)
  return new_order
  

count_swaps = 0
#print(is_good(order))
while is_good(order) != True:
  #for "L"
  if order.find("L",order.find("M")) != -1:
    order = swap(order,order.find("L",order.find("M")),order.find("M"))
    count_swaps += 1
    if order.find("L",order.find("S")) != -1:
      order = swap(order,order.find("L",order.find("S")),order.find("S"))
      count_swaps += 1
  elif order.find("L",order.find("S")) != -1:
    order = swap(order,order.find("L",order.find("S")),order.find("S"))
    count_swaps += 1
  if order.find("M",order.find("S")) != -1:
    order = swap(order,order.find("M",order.find("S")),order.find("S"))
    count_swaps += 1

print(count_swaps)

"""
LMMMS

LLSLM
"""