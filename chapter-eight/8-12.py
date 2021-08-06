# -*- coding: utf-8 -*-
# @Time : 2021/8/6 17:27
# @Author : Jamerri
# @File : 8-12.py


def sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)


sandwich('beef')
sandwich('beef', 'tomato', 'potato')
sandwich('ice cream', 'noodles')