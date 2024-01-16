"""
Name: Nrushanth Suthaharan
Date: Jan 12, 2023
Description: 2015 CCC J3
"""

consonants = "bcdfghjklmnpqrstvwxyz"
alphabet = "abcdefghijklmnopqrstuvwxyz"

word =input()
newWord = ""

for i in range(len(word)):
  current = word[i]
  newWord += current
  if(current in consonants):
    if(current == "b" or current == "c"):
      newWord += "a"
    elif(current == "d" or current == "f" or current == "g"):
      newWord += "e"
    elif(current == "h" or current == "j" or current == "k" or current == "l"):
      newWord += "i"
    elif(current == "m" or current == "n" or current == "p"  or current == "q" or current == "r"):
      newWord += "o"
    else:
      newWord += "u"

    if(current == "z"):
      newWord += "z"
    else:
      newWord += consonants[consonants.index(current)+1]

print(newWord)
  
  