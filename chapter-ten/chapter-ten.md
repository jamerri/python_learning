# 从文件中读取数据

要使用文本文件中的信息，首先需要将信息读取到内存中。可以全部读取，也可以每次一行的方式读取。

## 读取整个文件

~~~python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
~~~

1. 以任何方式打开文件
2. open()打开文件，close()关闭文件。注意！不能过早关闭文件。

## 文件路径

1. 要区分绝对路径和相对路径。

## 逐行读取

~~~python
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
~~~

## 创建一个包含文件各行内容的列表

~~~python
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
~~~

## 使用文件的内容

~~~python
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
~~~

## 包含一百万位的大型文件

# 写入文件

## 写入空文件

~~~python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming")
~~~

## 写入多行

~~~python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
~~~

## 附加到文件

~~~python
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
~~~

1. 注意这里面'w'改为了'a'，意思是从之前的文本接着往里面写入内容。

# 异常

## 处理ZeroDivisionError异常

1. 如果用0来作除数将会报这个错误。

## 使用try-except代码块

~~~python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
~~~

## 使用异常避免崩溃

## else代码块

~~~python
print("Give me two numbers, amd I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0")
    else:
        print(answer)
~~~

## 处理FileNotFoundError异常

~~~python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " dose not exist."
    print(msg)
~~~

## 分析文本

1. 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。

## 使用多个文件

1. 将上述功能封装为函数。

## 失败时一声不吭

1. 使用pass就直接跳过。

## 决定报告哪些错误

# 存储数据

## 使用json.dump()和json.load()

1. 函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象。

~~~python
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
~~~

## 保存和读取用户生成的数据

## 重构

