# -*- coding: utf-8 -*-
# @Time : 2021/8/4 16:39
# @Author : Jamerri
# @File : 6-5.py

rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'huanghe': 'china',
    }

for name, country in rivers.items():
    print('The ' + name.title() + ' runs through ' + country.title() + '.')

for name in rivers.keys():
    print(name)

for country in rivers.values():
    print(country)

