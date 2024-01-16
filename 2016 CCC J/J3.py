"""
Name: Nrushanth Suthaharan
Date: Dec 1, 2022
Description: J3 2016 CCC
"""
def is_palindrome(word):
  reversed_word = word[::-1]
  if(reversed_word == word):
    return True
  else:
    return False




word = input()
current = word
count = len(word)
statement = True
for i in range(len(word),0,-1):
  for j in range(len(word)-i):
    if(is_palindrome(word[])):

"""
banana

abracadabra
"""

