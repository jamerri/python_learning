# -*- coding: utf-8 -*-
# @Time : 2021/8/8 16:53
# @Author : Jamerri
# @FileName: name_function.py
# @Email : jamerri@163.com
# @Software: PyCharm


def get_formatted_name(first, last):
    """生成整洁的名字"""
    full_name = first + ' ' + last
    return full_name.title()