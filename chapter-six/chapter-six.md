# 一个简单的字典

~~~python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
~~~

# 使用字典

1. 在Python中，字典用放在花括号{}中的一系列键-值对表示。

## 访问字典中的值

## 添加键-值对

~~~python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
~~~

## 先创建一个空字典

~~~python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
~~~

## 修改字典中的值

## 删除键-值对

~~~python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
~~~

1. 删除的键-值对永远消失了。

## 由类似对象组成的字典

# 遍历字典

## 遍历所有的键-值对

~~~python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
~~~
1. for key, value in user_0.items() 这句中的key value是可以进行简写的。

## 遍历字典中的所有键

~~~python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())
~~~

1. for name in favorite_languages.keys() 这句话中的keys()代表了遍历键。

## 按顺序遍历字典中的所有键

~~~python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title())
~~~

## 遍历字典中的所有值

~~~python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
~~~

1. for language in favorite_languages.values() 这句话中的values()代表了遍历值。
2. favorite_languages.values()在这个地方加入set()就可以将重复的值进行剔除。

# 嵌套

## 字典列表

~~~python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
~~~

## 在字典中存储列表

## 在字典中存储字典