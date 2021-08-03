# 遍历整个列表

~~~python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
~~~

## 深入地研究循环

1. 使用单数和复数式名称，可帮助判断代码段处理地是单个列表元素还是整个列表。

## 在for循环中执行更多的操作

1. 一定要注意缩进。

# 避免缩进错误

## 忘记缩进

## 忘记缩进额外的代码行

## 不必要的缩进

## 循环后不必要的缩进

## 遗漏了冒号

# 创建数字列表

## 使用函数range()

~~~python
for value in range(1,5):
	print(vlaue)
~~~

1. 实际不会打印出5这个数字。

## 使用range()创建数字列表

1. 直接可以使用list()将range()转换为列表。

## 对数字列表执行简单的统计计算

1. min()、max()、sun()。

## 列表解析

~~~python
squares = [value**2 for value in range(1,11)]
print(squares)
~~~

# 使用列表的一部分

## 切片

1. [1:4] 指提取列表第2个到第4个元素。
2. [:4]指提取列表从头到第4个元素。
3. [1:]指提取列表从第2个到最后的元素。
4. [-3:]指提取列表倒数第3个元素到最后的元素。

## 遍历切片

~~~python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
~~~

## 复制列表

1. A = B[:]这样才可以进行复制，进行后续操作。

# 元组

**不可变的列表称为元组** 

## 定义元组

1. 试图改变元组的元素值将会报错。

## 遍历元组中的所有值

1. 与列表的操作一致。

## 修改元组变量

1. 相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。

# 设置代码格式

## 格式设置指南

## 缩进

**非常重要！！！**
**非常重要！！！**
**非常重要！！！**

## 行长

## 空行

## 其他格式设置指南