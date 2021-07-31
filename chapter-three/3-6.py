# -*- coding: utf-8 -*-
# @Time : 2021/7/31 23:00
# @Author : Jamerri
# @File : 3-6.py

Names = ['Sam', 'Bob', 'Tony']
print('Dear ' + Names[0] + ', do you like to eat dinner with me?')
print('Dear ' + Names[1] + ', do you like to eat dinner with me?')
print(Names[2] + ' can not eat dinner with me!')
Names[2] = 'John'
print('Dear ' + Names[2] + ', do you like to eat dinner with me?')
print('I find a bigger table!')
Names.insert(0, 'Amy')
Names.insert(2, 'Dodo')
Names.append('Jam')
for i in range(len(Names)):
    print('Dear ' + Names[i] + ', do you like to eat dinner with me?')