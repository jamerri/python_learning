# -*- coding: utf-8 -*-
# @Time : 2021/8/5 22:03
# @Author : Jamerri
# @File : 8-2.py


def favorite_book(title):

    print("One of my favorite books is " + title + " in Wonderland.")


favorite_book("Alice")

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')