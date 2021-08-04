# -*- coding: utf-8 -*-
# @Time : 2021/8/4 16:34
# @Author : Jamerri
# @File : 6-4.py

dicts = {
    'algorithm': '算法',
    'array': '数组',
    'bit': '位',
    'callback': '回调',
    'database': '数据库'
    }

# print('algorithm 的中文是：' + dicts['algorithm'] + '。')
# print('array 的中文是：' + dicts['array'] + '。')
# print('bit 的中文是：' + dicts['bit'] + '。')
# print('callback 的中文是：' + dicts['callback'] + '。')
# print('database 的中文是：' + dicts['database'] + '。')

for name in dicts.keys():
    print('编程术语为：' + name.title())

for meaning in dicts.values():
    print('编程术语对应的中文意思为：' + meaning)

dicts['for'] = '循环'
dicts['if'] = '如果'
dicts['reverse'] = '逆序'
dicts['set'] = '提取不是重复的信息'
dicts['key'] = '键'

print(dicts)