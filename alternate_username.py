#!/usr/bin/python3

cont_username = 5
x = 0
for l in range(0, 133):
    if x < cont_username:
        print("carlos")
        x += 1
    else:
        print("wiener")
        x=0

print("")
print ("==================================================================")
print("")


f = open('password.txt','r')
x = 0
count_password = 5
for line in f:
    if x < count_password:
        print(line,end="")
        x += 1
    else:
        print("peter")
        print(line,end="")
        x=0
