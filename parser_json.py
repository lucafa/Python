luca@luca-desktop:~/Programmi/Padelspot$ cat parser2.py 
#/usr/bin/python3

import json

with open('./xxxxxxxxyyyyyyyyyy','r') as string:
    my_dict=json.load(string)
string.close()

def iterate_multidimensional(my_dict):
    for k,v in my_dict.items():
        if(isinstance(v,dict)):
            print(k+":")
            iterate_multidimensional(v)
            continue
        print(k+" : "+str(v))

iterate_multidimensional(my_dict)
