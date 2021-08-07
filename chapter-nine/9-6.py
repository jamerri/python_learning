# -*- coding: utf-8 -*-
# @Time : 2021/8/7 22:52
# @Author : Jamerri
# @File : 9-6.py
# @Email : jamerri@163.com
# @Software : Pycharm


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors

    def describe_restaurant(self):
        print("The restaurant_name is " + self.restaurant_name.title())
        print("The cuisine_type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is opening!!!")

    def show_IceCream_type(self):
        for flavore in self.flavors:
            print("The favorite Icecream is " + flavore.title() + ".")


flavors = ['A', 'B', 'C']
IceCreamStand = Restaurant('Lili', 'Icecream', flavors)
IceCreamStand.show_IceCream_type()