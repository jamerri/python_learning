# -*- coding: utf-8 -*-
# @Time : 2021/8/6 17:31
# @Author : Jamerri
# @File : 8-13.py


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return  profile


user_profile = build_profile('Mingrui', 'Jiang', location='Nanjing', field='Engineering')
print(user_profile)
