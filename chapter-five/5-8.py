# -*- coding: utf-8 -*-
# @Time : 2021/8/3 19:33
# @Author : Jamerri
# @File : 5-8.py

users = ['admin', 'Eric', 'Bob', 'Amy', 'Sam']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + user + ', thank you for logging in again')
