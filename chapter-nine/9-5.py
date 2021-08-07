# -*- coding: utf-8 -*-
# @Time : 2021/8/7 19:47
# @Author : Jamerri
# @FileName: 9-5.py
# @Email : jamerri@163.com
# @Software: PyCharm


class User():
    def __init__(self, first_name, last_name, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print("The person name is " + self.first_name + " " + self.last_name + ".")

    def greet_user(self):
        if self.sex.title() == 'Man':
            print("Hello " + self.first_name + " man!")
        else:
            print("Hello " + self.first_name + " woman!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset__login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print("The login_attempts is " + str(self.login_attempts))


person = User('Mingrui', 'Jiang', 'man')
person.describe_user()
person.greet_user()

person.increment_login_attempts()
person.read_login_attempts()

person.increment_login_attempts()
person.read_login_attempts()

person.increment_login_attempts()
person.read_login_attempts()

person.reset__login_attempts()
person.read_login_attempts()