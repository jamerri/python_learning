# -*- coding: utf-8 -*-
# @Time : 2021/8/6 17:32
# @Author : Jamerri
# @File : 8-14.py

def make_car(manufacturer, car_type, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['manufacturer_name'] = manufacturer
    profile['car_type'] = car_type
    for key, value in user_info.items():
        profile[key] = value
    return  profile


user_profile = make_car('Audi', 'A4', color='red', tow_package='True')
print(user_profile)