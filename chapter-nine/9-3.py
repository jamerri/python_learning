# -*- coding: utf-8 -*-
# @Time : 2021/8/7 17:23
# @Author : Jamerri
# @FileName: 9-3.py
# @Email : jamerri@163.com
# @Software: PyCharm


class User():
    def __init__(self, first_name, last_name, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def describe_user(self):
        print("The person name is " + self.first_name + " " + self.last_name + ".")

    def greet_user(self):
        if self.sex.title() == 'Man':
            print("Hello " + self.first_name + " man!")
        else:
            print("Hello " + self.first_name + " woman!")


person = User('Mingrui', 'Jiang', 'man')
person.describe_user()
person.greet_user()
person = User('Yuguo', 'Wu', 'woman')
person.describe_user()
person.greet_user()
person = User('Yixiang', 'Wu', 'man')
person.describe_user()
person.greet_user()