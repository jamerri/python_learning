# -*- coding: utf-8 -*-
# @Time : 2021/8/3 19:42
# @Author : Jamerri
# @File : 5-10.py

current_users = ['Jamerri', 'Eric', 'Bob', 'Amy', 'Sam']
new_users = ['Jamerri', 'Eric', 'Dodo', 'John', 'Tony']

for new_user in new_users:
    if new_user in current_users or new_user.lower() in current_users or new_user.upper() in current_users:
        print('The name is used!')
    else:
        print('The name is not used!')
