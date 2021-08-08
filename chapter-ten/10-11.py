# -*- coding: utf-8 -*-
# @Time : 2021/8/8 16:17
# @Author : Jamerri
# @FileName: 10-11.py
# @Email : jamerri@163.com
# @Software: PyCharm

import json

number = input("What is your favorite number?")

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
with open(filename) as f_obj:
    favorite_num = json.load(f_obj)
print("I know your favorite number! It's " +number + ".")
