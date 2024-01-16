"""
Name: Nrushanth Suthaharan
Date: Feb 2, 2023
Description: J4 2015 CCC
"""


count = int(input())
word = []
commands = []
output = []

for i in range(count):
  command = input()
  word.append(command)
  current_friend = command[2:]
  if(command[0] != "W"):
    commands.append(current_friend)
time = 0
new = 0
for i in range(count):
  current = word[i]
  if current[0] == "W":
    time -= 1
    time += int(current[2:])
  else:
    current += " " + str(time)
    commands[new] += " " + str(time)
    new += 1
    time += 1
  word[i] = current

commands = sorted(commands)
count2 = 0
for i in range(len(commands)-1,0,-1):
  total_time = 0
  current_command = commands[i]
  new_command = commands[i-1]
  if(new_command[:2] == current_command[:2]):
    total_time = abs(int(current_command[2:])-int(new_command[2:]))
    print(total_time)
  output.append(current_command[:2] + str(total_time))
  

  
print(word)
print (commands)
#print(sorted(commands))

#for i in range(len(output)):
#  print(output[i])
"""
5
R 2
R 3
W 5
S 2
S 3

##

14
R 12
W 2
R 23
W 3
R 45
S 45
R 45
S 23
R 23
W 2
S 23
R 34
S 12
S 34
"""