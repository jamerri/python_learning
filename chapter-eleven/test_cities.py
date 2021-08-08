# -*- coding: utf-8 -*-
# @Time : 2021/8/8 22:20
# @Author : Jamerri
# @File : test_cities.py
# @Email : jamerri@163.com
# @Software : Pycharm

import unittest
from city_functions import city_country_function


class test_city_country(unittest.TestCase):
    """测试city_functions.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        city_country_name = city_country_function('Santiago', 'Chile', 5000000)
        self.assertEqual(city_country_name, 'Santiago, Chile -population 5000000')


unittest.main()