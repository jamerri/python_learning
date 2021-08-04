# -*- coding: utf-8 -*-
# @Time : 2021/8/4 20:10
# @Author : Jamerri
# @File : 7-4.py

pizzas = "\nWhat kind of pizza do you want to eat?"
pizzas += "\nEnter 'quit' to end the program."
message = " "
while message != 'quit':
    message = input(pizzas)
    print("We will join " + message + " in pizza!")