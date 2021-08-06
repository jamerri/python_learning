# -*- coding: utf-8 -*-
# @Time : 2021/8/5 23:05
# @Author : Jamerri
# @File : 8-5.py


def describe_city(city_name, city_country='china'):
    print(city_name.title() + " is in " + city_country.title())


describe_city('Nanjing')
describe_city('Shanghai')
describe_city('Reykjavik', 'Iceland')