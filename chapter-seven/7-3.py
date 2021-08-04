# -*- coding: utf-8 -*-
# @Time : 2021/8/4 19:56
# @Author : Jamerri
# @File : 7-3.py

num = input("Please input a number：")
num = int(num)
if num % 10 == 0:
    print(str(num) + '是10的倍数。')
else:
    print(str(num) + '不是10的倍数。')