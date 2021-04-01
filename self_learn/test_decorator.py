"""
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
把函数赋值给变量时，函数名后面可带()也可不带,当函数名后带了()时，变量调用就不能加()；当函数名后不带()时，变量调用就要加()。参考以下四种：
"""

def now():
    print('2021-03-30')
#1 正确，有打印信息,最常用的函数名赋值给变量
a = now
a()

#2 不会报错，但是没有打印信息
# a = now
# a

#3 正确，有打印信息
# a = now()
# a

#4 报错，这样赋值后 a()就相当于now()()
# a = now()
# a()

# 函数对象有一个__name__属性，可以拿到函数的名字，注意是用函数名，而非 函数名().__name__
# print(now.__name__)
# print(a.__name__)

# 在学习装饰器decorator之前，先来了解下python中的(*args, **kwargs) 参数。
# 这两个是python中的可变参数。*args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。
# 当同时使用*args和**kwargs时，必须*args参数列要在**kwargs前，像foo(a=1, b='2', c=3, a', 1, None, )这样调用的话，
# 会提示语法错误“SyntaxError: non-keyword arg after keyword arg”
# def foo(*args, **kwargs):
#     print('args = ',args)
#     print('kwargs = ',kwargs)
#     print('---------------------')
#
# if __name__ == '__main__':
#    foo(1,2,3,4)
#    foo(a=1,b=2,c=3)
#    foo(1,2,3,4, a=1,b=2,c=3)
#    foo('a', 1, None, a=1, b='2', c=3)

# python中有内置的装饰器，也可以自定义装饰器供后面代码中用，比如
# def log(func):
#     print('call %s():' % func.__name__)
#     return func
#
# @log
# def plus(a, b):
#     c = a + b
#     print(c)
#
# # print(plus(1, 2))
# plus(1, 2)


def maker(N):
   def action(X):
      return X**N
   return action

f = maker(2)
f(3)










