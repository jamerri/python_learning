# -*- coding: utf-8 -*-
# @Time : 2021/8/8 15:46
# @Author : Jamerri
# @FileName: 10-6.py
# @Email : jamerri@163.com
# @Software: PyCharm

print("Give me two numbers, amd I'll add them.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("The input is not number")
else:
    print(answer)
