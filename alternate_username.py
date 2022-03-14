#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f","--fileused", help="File to be used", required=True)
parser.add_argument("-u","--username", help="Username to insert every x elements", required=True)
parser.add_argument("-c","--count_element", type=int, help="Number of line to alternate insert betwen one username and other", required=True)

args = parser.parse_args()

filename = args.fileused
cont_username = args.count_element
username = args.username

f = open(filename,'r')
x = 0

for line in f:
    if x < cont_username:
        print(line,end="")
        x += 1
    else:
        print(username)
        x=0
