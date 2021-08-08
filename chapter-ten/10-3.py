# -*- coding: utf-8 -*-
# @Time : 2021/8/8 14:49
# @Author : Jamerri
# @FileName: 10-3.py
# @Email : jamerri@163.com
# @Software: PyCharm

filename = 'guestname.txt'

print("-------Hello everyone-------")
guest_name = input("Please input your name: ")

with open(filename, 'w') as file_object:
    file_object.write("guest name is " + guest_name.title())
