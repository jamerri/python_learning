# -*- coding: utf-8 -*-
# @Time : 2021/8/7 17:21
# @Author : Jamerri
# @FileName: 9-2.py
# @Email : jamerri@163.com
# @Software: PyCharm


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant_name is " + self.restaurant_name.title())
        print("The cuisine_type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is opening!!!")


My_restaurant_1 = Restaurant('Lisa', 'Chinese food')
My_restaurant_1.describe_restaurant()
My_restaurant_2 = Restaurant('Timi', 'Japan food')
My_restaurant_2.describe_restaurant()
My_restaurant_3 = Restaurant('Dodo', 'Mexico food')
My_restaurant_3.describe_restaurant()
