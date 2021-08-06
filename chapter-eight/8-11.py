# -*- coding: utf-8 -*-
# @Time : 2021/8/6 16:39
# @Author : Jamerri
# @File : 8-11.py

magicians = ['David', 'Alice', 'Tony']
make_great_magicians = []


def show_magicians(magicians):
    for magician in magicians:
        magicians.pop()
        make_great_magicians.append(make_great(magician))


def make_great(magician):
    make_great_magician = ("The Great " + magician.title())
    return make_great_magician


show_magicians(magicians[:])
print(magicians)
print(make_great_magicians)