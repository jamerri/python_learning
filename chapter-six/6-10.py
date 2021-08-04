# -*- coding: utf-8 -*-
# @Time : 2021/8/4 17:02
# @Author : Jamerri
# @File : 6-10.py

love_num = {
    'Sam': [12, 18, 29],
    'Amy': [2, 16, 25],
    'Jamerri': [7, 17, 27],
    'Tony': [4, 6, 19],
    'Bob': [1, 11, 21],
    }

for name, nums in love_num.items():
    print(name.title() + "'s love number are:")
    for num in nums:
        print("\t" + str(num))
