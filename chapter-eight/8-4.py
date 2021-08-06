# -*- coding: utf-8 -*-
# @Time : 2021/8/5 23:03
# @Author : Jamerri
# @File : 8-4.py


def make_shirt(shirt_size, shirt_type='animal'):
    print("T_shirt's size is " + shirt_size.title() + ", T_shirt's type is " + shirt_type.title() + ".")


make_shirt('L')
make_shirt('M')
make_shirt('M', shirt_type='fruit')