# -*- coding: utf-8 -*-
# @Time : 2021/8/4 20:51
# @Author : Jamerri
# @File : 7-10.py

responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的姓名和回答
    name = input("\nWhat is your name? ")
    response = input("Which place would you like to someday? ")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to " + response + ".")