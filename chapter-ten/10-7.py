# -*- coding: utf-8 -*-
# @Time : 2021/8/8 15:50
# @Author : Jamerri
# @FileName: 10-7.py
# @Email : jamerri@163.com
# @Software: PyCharm

print("Give me two numbers, amd I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("The input is not number")
    else:
        print(answer)