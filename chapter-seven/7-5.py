# -*- coding: utf-8 -*-
# @Time : 2021/8/4 20:14
# @Author : Jamerri
# @File : 7-5.py

words = "How old are you?"
age = " "

while age != 'quit':
    age = input(words)
    if age == 'quit':
        break
    if int(age) < 3:
        print("No need buy ticket")
    elif int(age) < 12:
        print("The ticket is 10 $")
    else:
        print("The ticket is 15 $")
