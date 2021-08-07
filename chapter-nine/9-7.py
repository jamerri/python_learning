# -*- coding: utf-8 -*-
# @Time : 2021/8/7 22:57
# @Author : Jamerri
# @File : 9-7.py
# @Email : jamerri@163.com
# @Software : Pycharm


class User():
    def __init__(self, first_name, last_name, privileges):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = privileges

    def describe_user(self):
        print("The person name is " + self.first_name + " " + self.last_name + ".")

    def greet_user(self):
        if self.sex.title() == 'Man':
            print("Hello " + self.first_name + " man!")
        else:
            print("Hello " + self.first_name + " woman!")


class Admin(User):

    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name, privileges)

    def show_privileges(self):
        print("The privileges is" + self.privileges)


person = Admin('Mingrui', 'Jiang', 'can add post')
person.show_privileges()
