# -*- coding: utf-8 -*-
# @Time : 2021/8/5 21:46
# @Author : Jamerri
# @File : __init__.py


# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止
#     打印每个设计后，都将其移到列表completed_models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# def make_pizza(*toppings):
#     """概述要制作的披萨"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green pepers', 'extra cheese')


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return  profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)