# -*- coding: utf-8 -*-
# @Time : 2021/8/4 19:45
# @Author : Jamerri
# @File : __init__.py

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = " "
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#
#     print(current_number)

# # 首先，创建一个待验证用户列表
# #  和一个用于存储已验证用户的空列表
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# # 验证每个用户，直到没有未验证用户为止
# #  将每个经过验证的列表都移到已验证用户列表中
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
#
# # 显示所有已验证的用户
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的姓名和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")