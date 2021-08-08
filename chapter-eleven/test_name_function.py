# -*- coding: utf-8 -*-
# @Time : 2021/8/8 16:57
# @Author : Jamerri
# @FileName: test_name_function.py
# @Email : jamerri@163.com
# @Software: PyCharm

import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()