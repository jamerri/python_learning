# -*- coding: utf-8 -*-
# @Time : 2021/8/8 13:34
# @Author : Jamerri
# @FileName: __init__.py.py
# @Email : jamerri@163.com
# @Software: PyCharm

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)