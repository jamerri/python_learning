# -*- coding: utf-8 -*-
# @Time : 2021/8/8 14:16
# @Author : Jamerri
# @FileName: 10-2.py
# @Email : jamerri@163.com
# @Software: PyCharm

file_name = 'learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())