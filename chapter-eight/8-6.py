# -*- coding: utf-8 -*-
# @Time : 2021/8/5 23:21
# @Author : Jamerri
# @File : 8-6.py


def city_country(city_name, country_name):
    full_name = city_name + ", " + country_name
    return full_name


city_full_name_1 = city_country('Luzhou', 'China')
city_full_name_2 = city_country('Nanjing', 'China')
city_full_name_3 = city_country('Shanghai', 'China')

print(city_full_name_1)
print(city_full_name_2)
print(city_full_name_3)
