# -*- coding: utf-8 -*-
# @Time : 2021/8/4 20:49
# @Author : Jamerri
# @File : 7-9.py

sandwich_orders = ['pastrami', 'hot dog', 'beef', 'pastrami', 'tomato', 'potato', 'pastrami']
finished_sandwichs = []

print("No the pastrami sandwich！")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwichs.append(current_sandwich)

print("\nThe sandwich have been finished:")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich.title() + " sandwich")