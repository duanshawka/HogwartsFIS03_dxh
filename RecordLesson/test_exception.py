"""
常见的python异常有：语法异常，名称异常，索引异常，键异常，值异常

# 语法异常 SyntaxError: invalid syntax
a = 10
if a >=10
print ("a>=10")

# 名称异常 NameError: name 'num' is not defined
a = 10
if num >=10:
   print ("a>=10")

# 索引异常:IndexError: list index out of range
list=[8,3,2]
print(list[3])

#键异常：KeyError: 'age'
dic={'name':'shawka'}
print(dic['age'])

# 值异常：ValueError: invalid literal for int() with base 10: 'aa'
a = input("请输入一个数：")
print(int(a))
"""



# 下面try里的语句块自上而下的执行，遇到异常，try里异常语句下的其他语句不执行，进入except语句块，
# 这个语句块是专门收集异常信息,然后执行finally语句。如果try语句块里没有异常抛出，就会跳过except语句去执行finally
# try，except，finally经常组合使用，try有异常，抛出异常给except接收，try无异常跳过except
# finally不管有没有异常最后必须执行的，一般用于之前打开了一个文件，后面关闭文件操作
# try:
#     def div(a,b):
#         return a/b
#     print(div(8,2))
#
#     # print(f.readlines())读取文件内容
#     f = open("data.txt")
#     print(f.readlines())
#
#     list = [3,8,2]
#     print(list[3])
#     # 上面语句有异常，所以没有执行打印"aaaa"
#     print("aaaa")
#
# except Exception as e:
#     print(e)
#
# finally:
#     print("finally")
#     f.close()



