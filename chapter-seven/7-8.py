# -*- coding: utf-8 -*-
# @Time : 2021/8/4 20:45
# @Author : Jamerri
# @File : 7-8.py

sandwich_orders = ['hot dog', 'beef', 'tomato', 'potato']
finished_sandwichs = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwichs.append(current_sandwich)

print("\nThe sandwich have been finished:")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich.title() + " sandwich")