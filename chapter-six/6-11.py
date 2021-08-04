# -*- coding: utf-8 -*-
# @Time : 2021/8/4 17:05
# @Author : Jamerri
# @File : 6-11.py

cities = {
    'Nanjing': {
        'country': 'China',
        'population': 10000000,
        'fact': '江苏省省会城市',
        },
    'Shanghai':{
        'country': 'China',
        'population': 20000000,
        'fact': '中国金融中心',
        },
    'Luzhou':{
        'country': 'China',
        'population': 4000000,
        'fact': '四川省地级市',
        },
    }

for name, information in cities.items():
    print(name.title() + 'is in ' + information['country'] + ', and population is ' + str(information['population']) + ', and its ' + information['fact'] + '。')