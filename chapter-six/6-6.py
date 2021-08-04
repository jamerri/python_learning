# -*- coding: utf-8 -*-
# @Time : 2021/8/4 16:43
# @Author : Jamerri
# @File : 6-6.py

person = ['jen', 'edward', 'phil']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    if name in person:
        print("Thanks for you very much, " + name.title() + "!")
    else:
        print("Would you like to join ?" + name.title() + ".")