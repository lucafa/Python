#!/usr/bin/python3
import re

#cfile = open ('./controllo.txt','r+')


def find_ip():
	f = open('./syslog','r')
	ip_address = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$')
	
	for line in f:
		mo = ip_address.search(line)
		if mo != None:
			print(mo.group())
			
		

find_ip()
