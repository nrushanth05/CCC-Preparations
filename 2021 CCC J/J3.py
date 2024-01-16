"""
Name: Nrushanth Suthaharan
Description: 2021 CCC J3
"""
numbers = []

rand_val = ""

direction = ""
string = ""
while rand_val != "99999":
    rand_val = (input())
    if rand_val == "99999":
        break
    else:
        numbers.append(rand_val)
        first_sum = int(rand_val[0]) + int(rand_val[1])
        if first_sum % 2 == 0 and first_sum != 0:
            direction = "right"
        elif first_sum % 2 != 0:
            direction = "left"
        elif first_sum == 0:
            direction = direction

        string += direction + " " + rand_val[2:] + "\n"

print(string)
"""
57234
00907
34100
99999


"""
