from collections import Iterable
# L = list(range(100))
# # 从上面的定义看出L为一个包含0，1，2到99一共100个数字的列表，
# # 求前10个数字：
# print(L[:10])
# # 求倒数后10个数字
# print(L[-10:])
# # 求列表中从第一个数字开始取，每隔一个数字取一个数字一直到取完为止。
# print(L[0:100:2])

# 元组和字符串也都可以用切片，切片后不改变原来数据类型，也即字符串切片后得到的还是字符串
# print(str[1:4])表示取出str中索引位置为1到3的字符串，也即第2位到第4位的字符串


str = 'ABCDEF'
print(str[1:4])

"""
给定一个list或者tuple，可以通过for...in 循环来遍历这个list或tuple，这种遍历我们称为迭代iteration
像list和tuple是有下标也即索引的数据类型，像没有下标的字典，只要是可迭代对象，也照样可以迭代
"""
l = ['ab','cd','ef']
for i in l:
    print(i)


d = {'a':1,
     'b':2,
     'c':3
     }
# 默认情况下，dict迭代的是key，如果要迭代value，要用 for value in d.values()
# 如果同时要迭代key和value，要用 for key，value in d.items()
for key in d:
    print (key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)

# 如何判断一个对象是不是可迭代对象，通过collections模块的iterable类型来判断
# 如下看出 字符串，元组，列表，字典都可以迭代，整数不可以
print(isinstance('abc',Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance([1, 2], Iterable))
print(isinstance({'a':1,'b':2}, Iterable))
print(isinstance(123, Iterable))

# python内置的enumerate函数可以把一个list/tuple变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
# 在python的for循环里面引用两个变量也是很常见的,有点迷糊这些迭代出来的数据怎么用？？
for i,value in enumerate(('A','B','C')):
    print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)


"""
---list() 函数用于将元组、区间（range）等转换为列表。range(n)表示从0到n-1的整数序列，一共有n个数字
a,b,c,d,e分别定义了 tuple元组，dict字典，set集合，range()区间，字符串
list(dict)  默认把字典的key转换成列表
---len(x)函数返回对象x的长度或者对象个数，x可以为元组/字典/集合/区间/字符串/列表
"""
a = (1,2)
b = {"1":2,"3":3}
c = {7,8,9}
d = range(2,10,2)
e = 'abcdef'
f = ['python','java','ruby']

# list()函数可对tuple元组，dict字典，set集合，range()区间，字符串转换
# print(list(a))
# print(list(b))
# print(list(c))
# print(list(d))
# print(list(e))

# len(x)返回对象x的长度或者个数
# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))
# print(len(e))

# strip() 方法用于移除字符串头尾指定的字符（无参数时默认为空格或换行符）或字符序列
# print(str3.strip('12')) 会在str3字符串的首尾找1和2的数据删掉，只要碰到不可以删的字符后就停止寻找
# str1 = '0003210Runoob012300'
# str2 = ' Runoob   '
# str3 = "123Runoob12321"
#
# print(str1.strip('0'))
# print(str2.strip())
# print(str3.strip('12'))

# 删除字典中的某个键值对，pop('key1'),如果key1不存在字典中，就会抛异常。
dict = {'x':1,'y':2,'z':3}
dict.pop('x')
print(dict)

dict.pop('1')

