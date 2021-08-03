# -*- coding: utf-8 -*-
# @Time : 2021/8/3 11:50
# @Author : Jamerri
# @File : 4-11.py

pizzas = ['potato', 'beef', 'peperoni']

for pizza in pizzas:
    print('I like ' + pizza + ' pizza!')

print('I really love pizza!')

pizzas.append('noodles')
print(pizzas)
friend_pizzas = pizzas[:]
print(friend_pizzas)
friend_pizzas.append('tomato')
print(pizzas)
print(friend_pizzas)
for pizza in pizzas:
    print('My favorite pizzas are: ' + pizza + ' pizza!')

for friend_pizza in friend_pizzas:
    print("My friend's favorite pizzas are: " + friend_pizza + ' pizza!')
