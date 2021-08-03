# -*- coding: utf-8 -*-
# @Time : 2021/8/3 19:40
# @Author : Jamerri
# @File : 5-9.py

# users = ['admin', 'Eric', 'Bob', 'Amy', 'Sam']
users = []

if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user + ', thank you for logging in again')
else:
    print('We need to find some users!')