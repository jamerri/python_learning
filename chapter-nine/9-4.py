# -*- coding: utf-8 -*-
# @Time : 2021/8/7 19:38
# @Author : Jamerri
# @FileName: 9-4.py
# @Email : jamerri@163.com
# @Software: PyCharm


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant_name is " + self.restaurant_name.title())
        print("The cuisine_type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is opening!!!")

    def read_number_served(self):
        print("The number in restaurant is " + str(self.number_served) + "!")

    def set_number_served(self, people_num):
        self.number_served = people_num

    def increment_number_served(self, delta_num):
        self.number_served += delta_num


restaurant = Restaurant('Lisa', 'Chinese food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(24)
restaurant.read_number_served()

restaurant.increment_number_served(2)
restaurant.read_number_served()