# -*- coding: utf-8 -*-
# @Time : 2021/8/8 14:08
# @Author : Jamerri
# @FileName: 10-1.py
# @Email : jamerri@163.com
# @Software: PyCharm

file_name = 'learning_python.txt'

"""方法一"""
with open(file_name) as file_object:
    content = file_object.read()
    file_object.close()
print(content)

"""方法二"""
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
    file_object.close()

"""方法三"""
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())