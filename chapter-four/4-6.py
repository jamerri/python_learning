# -*- coding: utf-8 -*-
# @Time : 2021/8/3 11:07
# @Author : Jamerri
# @File : 4-6.py

"""方法1"""
odd_nums = []
for odd_num in range(1, 20, 2):
    print(odd_num)
    odd_nums.append(odd_num)
print(odd_nums)

"""方法2"""
odd_nums = [odd_num for odd_num in range(1, 20, 2)]
print(odd_nums)
for i in range(len(odd_nums)):
    print(odd_nums[i])