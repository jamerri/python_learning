# 测试函数

## 单元测试和测试用例

1. Python标准库中的模块unittest提供了代码测试工具。
2. 单元测试用于核实函数的某个方面没有问题。
3. 测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。

## 可通过的测试

1. 要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个继承unittest.

~~~python
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase)
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
unittest.main()
~~~

## 不能通过的测试

## 测试未通过时怎么办

## 添加新测试

# 测试类

## 各种断言方法

|          方法           |        用途        |
| :---------------------: | :----------------: |
|    assertEqual(a, b)    |     核实a == b     |
|  assertNotEqual(a, b)   |     核实a != b     |
|      assertTrue(x)      |    核实x为True     |
|     assertFalse(x)      |    核实x为False    |
|  assertIn(item, list)   |  核实item在list中  |
| assertNotIn(item, list) | 核实item不在list中 |

## 一个要测试的类

## 测试AnonymousSurvey类

## 方法Setup()