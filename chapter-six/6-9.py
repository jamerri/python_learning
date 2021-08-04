# -*- coding: utf-8 -*-
# @Time : 2021/8/4 16:57
# @Author : Jamerri
# @File : 6-9.py

favorite_places = {
    'wang': ['Lijiang', 'Shanghai', 'Haikou'],
    'li': ['Dali', 'Yangzhou', 'Chongqing'],
    'tang': ['Chengdu', 'Nanjing', 'Wuhan']
}

for name, citys in favorite_places.items():
    print(name.title() + "'s favorite_places are:")
    for city in citys:
        print("\t" + city.title())