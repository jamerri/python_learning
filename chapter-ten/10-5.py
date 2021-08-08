# -*- coding: utf-8 -*-
# @Time : 2021/8/8 15:01
# @Author : Jamerri
# @FileName: 10-5.py
# @Email : jamerri@163.com
# @Software: PyCharm

filename = 'reason.txt'
key = True

print("-------Hello everyone-------")
while key:
    reason = input("Please input why you love programming: ")
    if reason != '':
        with open(filename, 'a') as file_object:
            file_object.write(reason.title() + ".\n")
    else:
        key = False
