# -*- coding: utf-8 -*-
# @Time : 2021/8/7 23:06
# @Author : Jamerri
# @File : 9-8.py
# @Email : jamerri@163.com
# @Software : Pycharm


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def describe_user(self):
        print("The person name is " + self.first_name + " " + self.last_name + ".")

    def greet_user(self):
        if self.sex.title() == 'Man':
            print("Hello " + self.first_name + " man!")
        else:
            print("Hello " + self.first_name + " woman!")


class Privileges():
    def __init__(self, privileges='can add post'):
        self.privileges = privileges

    def show_privileges(self):
        print("The privileges is" + self.privileges + ".")


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


person = Admin('Mingrui', 'Jiang')
person.privileges.show_privileges()