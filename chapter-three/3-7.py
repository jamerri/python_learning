# -*- coding: utf-8 -*-
# @Time : 2021/7/31 23:03
# @Author : Jamerri
# @File : 3-7.py

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

print('The table can not arrive at time! I just invite two people with me eating dinner!')

del_people_name = Names.pop(0)
print('I am very sorry, dear ' + del_people_name + '!')
del_people_name = Names.pop(0)
print('I am very sorry, dear ' + del_people_name + '!')
del_people_name = Names.pop(0)
print('I am very sorry, dear ' + del_people_name + '!')
del_people_name = Names.pop(0)
print('I am very sorry, dear ' + del_people_name + '!')
print(Names)
print('Dear ' + Names[0] + ', you are always in list!')
print('Dear ' + Names[1] + ', you are always in list!')

del Names[0]
print(Names)

del Names[0]
print(Names)
