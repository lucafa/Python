#!/usr/bin/python3

x = 0
for l in range(0, 133):
    if x < 2:
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
for line in f:
    if x < 1:
        print(line,end="")
        x += 1
    else:
        print("peter")
        print(line,end="")
        x=0

