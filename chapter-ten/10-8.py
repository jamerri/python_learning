# -*- coding: utf-8 -*-
# @Time : 2021/8/8 15:57
# @Author : Jamerri
# @FileName: 10-8.py
# @Email : jamerri@163.com
# @Software: PyCharm

filenames = ["cats.txt", "dogs.txt"]
for filename in filenames:
    try:
        with open(filename) as file_obj1:
            names = file_obj1.readlines()
            for name in names:
                print(name.rstrip())
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " dose not exist."
        print(msg)