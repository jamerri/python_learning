# -*- coding: utf-8 -*-
# @Time : 2021/8/8 22:19
# @Author : Jamerri
# @File : city_functions.py
# @Email : jamerri@163.com
# @Software : Pycharm


def city_country_function(city, country, population=''):
    if population:
        city_country_name = city + ", " + country + " -population " + str(population)
    else:
        city_country_name = city + ", " + country
    return city_country_name
