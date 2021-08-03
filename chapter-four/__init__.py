# -*- coding: utf-8 -*-
# @Time : 2021/8/2 22:24
# @Author : Jamerri
# @File : __init__.py

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

squares = [value ** 2 for value in range(1, 11)]
print(squares)

odd_nums = [odd_num for odd_num in range(1, 20, 2)]
print(odd_nums)
for i in range(len(odd_nums)):
    print(odd_nums[i])

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
