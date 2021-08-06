# 定义函数

~~~python
def greet_user():
    """显示简单的问候语"""
    print("Hello!")

greet_user()
~~~

## 向函数传递信息

~~~python
def greet_user(username):
    """显示简单的问候语"""
    print("Hello!" + username.title() + "!")

greet_user('jesse')
~~~

## 实参和形参

1. 'username'是形参，'jesse'是实参。

# 传递实参

## 位置实参

① 调用函数多次
② 位置实参的顺序很重要

## 关键字实参

## 默认值

## 等效的函数调用

## 避免实参错误

# 返回值

## 返回简单值

## 让实参变成可选的

## 返回字典

## 结合使用函数和while循环

# 传递列表

~~~python
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
~~~

## 在函数中修改列表

~~~python
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
~~~

## 禁止函数修改列表

1. function_name(list_name[:])

# 传递任何数量的实参

~~~python
def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepers', 'extra cheese')
~~~

## 结合使用位置实参和任意数量实参

~~~python
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pepers', 'extra cheese')
~~~

1. 基于上述函数定义，Python将受到的第一个值存储在形参size中，并将其他的所有值都存储在元组toppings中。

## 使用任意数量的关键字实参

~~~python
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return  profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
~~~

# 将函数存储在模块中

## 导入整个模块

1. 将文件A.py中除函数function_name()之外的其他代码删除。
2. 在B.py文件中导入刚创建的模块，再调用函数。
3. module_name.function_name()

## 导入特定的函数

1. from module_name import function_name
2. from module_name import function_name_0, function_name_1, function_name_2

## 使用as给函数指定别名

1. from module_name import function_name as fn

## 导入模块中的所有函数

1. from module_name import *

## 函数编写指南

1. 给形参指定默认值时，等号两边不要有空格：def funcrion_name(parameter_0, parameter_1='default value')
2. 对于函数调用中的关键字实参，也应遵循这种约定：funcrion_name(value_0, parameter_1='value'）