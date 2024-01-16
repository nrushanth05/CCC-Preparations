"""
Name: Nrushanth Suthaharan
Description: 2022 CCC J3
"""
single_line = input()


list_line = list(single_line)

line = single_line

list_instructs = []
length = 0
for i in range(len(single_line)):
    if single_line[i].isnumeric():
      stop = i+1
      while len(single_line) > stop and single_line[stop].isnumeric():
          stop += 1
      instruct = single_line[length:stop]
      if len(instruct) != 0:
        list_instructs.append(instruct)
      #line = line[i+1:]
      length += len(instruct)

#print(list_instructs)
    
for i in range(len(list_instructs)):
  current_instruct = list_instructs[i]
  if "+" in current_instruct:
    index_sign = current_instruct.find("+")
    sign = "tighten"
  elif "-" in current_instruct:
    index_sign = current_instruct.find("-")
    sign = "loosen"
  letters = current_instruct[:index_sign]
  num = current_instruct[index_sign+1:]
  print(letters + " "+sign+ " "+ num)

"""
AFB+8HC-4

AFB+8SC-4H-2GDPE+9

AFB+88HC-444
"""
  
  