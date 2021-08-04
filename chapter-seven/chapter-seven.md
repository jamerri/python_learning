# 函数input()的工作原理

~~~python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
~~~

1. 函数input()接受一个参数：即要向显示的提示或说明。等待用户输入后按回车键后继续进行。

## 编写清晰的程序

1. 字符串可以使用+=符号。

## 使用int()来获取数值输入

1. 输入的内容直接用int()函数继续变换。

## 求模运算符

1. 求模运算符（%）是一个很有用的工具，它将两个数相除并返回余数。

# While循环简介

## 使用while循环

~~~python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
~~~

1. while是只要满足这个条件就将一直运行。

## 让用户选择何时退出

~~~python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = " "
while message != 'quit':
    message = input(prompt)
    print(message)
~~~

## 使用标志

1. 可以通过True和False来决定循环是否继续运行。

## 使用break退出循环

1. break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行。

## 在循环中使用continue

~~~python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
~~~

## 避免无限循环

1. 如果不小心陷入了无限循环，可以通过Ctrl+C结束程序运行。

# 使用while循环来处理列表和字典

## 在列表之间移动元素

~~~python
# 首先，创建一个待验证用户列表
#  和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
#  将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
~~~

## 删除包含特定值的所有列表元素

~~~python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
~~~

## 使用用户输入来填充字典

~~~python
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的姓名和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
~~~