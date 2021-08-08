# -*- coding: utf-8 -*-
# @Time : 2021/8/8 14:53
# @Author : Jamerri
# @FileName: 10-4.py
# @Email : jamerri@163.com
# @Software: PyCharm

filename = 'guest_book.txt'
key = True

print("-------Hello everyone-------")
while key:
    guest_name = input("Please input your name: ")
    if guest_name != 'q':
        print("Hello " + guest_name)
        with open(filename, 'a') as file_object:
            file_object.write("guest name is " + guest_name.title() + ".\n")
    else:
        key = False
