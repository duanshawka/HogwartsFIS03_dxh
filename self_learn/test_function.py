"""
Python内置了很多有用的函数，我们可以直接调用。
要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。
调用一个函数用: 函数名(参数)
调用函数的时候，如果传入的参数数量/或者参数数据类型不能被函数接受，都会报TypeError的错误，如下：
abs(1, 2)
TypeError: abs() takes exactly one argument (2 given)
abs('a')
TypeError: bad operand type for abs(): 'str'
"""

# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(bool(1))
print(bool(''))