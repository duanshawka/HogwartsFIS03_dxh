"""
import os
# 打印当前文件的路径，os.path.dirname(__file__),具体到当前文件最近的上一级目录，包或者文件
def test_get_path():
  file_path = os.path.dirname(__file__)
  print(file_path)

test_get_path()
"""
# 变量和函数：
# - Python允许模块里定义变量和函数
# - 函数里是可以调用外部的变量，但不允许修改外部变量
# - 通过id()方法可是打印对象的内存地址
# - 方法默认返回值为None

# a = 1
# def func():
#    print(f"函数里可以调用外部变量，a的值为{a}")
#    print(id(a))
#
# print(a)
# print(id(a))
# func()
# print(func())比直接调用func()函数多一个None返回值，说明方法有个默认返回值None
# print(func())

# 在函数里把外部变量global之后就可以在函数里对外部变量进行修改
# 下面的调用中会返回三个id，第一个print(id(a))和第二个print(id(a))返回的id不一样----原因：不同值哪怕相同变量名前后的内存地址不一样
# 第二个print(id(a))和调用func()返回的id是一样的。
# 所以以func()的调用为界限，修改了外部变量a的值，变量a指向的内存地址由1变成2
# a = 1
# def func():
#   global a
#   a = 2
#   print(id(a))
#   print(f"函数里修改了外部变量a，a的值为{a}")
#
# print(a)
# print(id(a))
# func()
# print(id(a))
# print(a)

# Python变量保存的是值的引用，不同变量相同值 其内存地址是相同的，比如变量a，b都引用了值1的内存空间。
# 变量的存储，采用了引用语义的方式，存储的只是一个变量的值所在的内存地址，而不是这个变量的值本身
# 我们把不同的值赋给变量时候，变量指向的地址发生变化，但是相同的值地址不发生变化。
a = 1
b = 1
c = 2
d = 2

print(id(a))
print(id(b))
print(id(c))
print(id(d))


