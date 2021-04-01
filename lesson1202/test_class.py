class Person:
    name:str = "default"
    sex:str = 'male'
    age:int = 0

    # 通过self.name调用类的属性，self.name可以叫实例变量，
    # 等式右边的name为外面实例化传进来的name，这样通过实例调用name就为实例特有的name了
    # def set_name(self,name):
    #     self.name = name

    # 但是上面方法非常麻烦，类的属性有多少个就要设置多少个set方法来给实例赋值，
    # 可用下面的构造函数代替,构造函数在实例化一个对象 'zs = Person()'的时候就会被调用
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    # 在类里面定义的方法要加self参数
    # @classmethod
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# 实例化一个人zs，传入的值的个数要和__init__构造函数中的参数个数一样多
zs = Person('zhangsan','男',20)

# 类变量 和 实例变量的区别：
# 类变量需要类来访问，实例变量需要实例来访问
print(Person.name)
print(zs.name)
# 类变量 实例变量 都可以被修改
Person.name = 'Tom'
zs.name = 'lily'
print(Person.name)
print(zs.name)

# 类中的方法不能用类访问，要用实例来访问（因为类中的方法是带了self参数的，相当于是实例方法）
# 若想Person.eat()可以使用，要对类中的方法eat加一个装饰器 @classmethod,只对eat方法起作用，
# sleep方法要变成类方法要另加一个 @classmethod
# 当类中的方法加上装饰器@classmethod后，该方法可以同时用类 和实例调用，但是结果是一样的。
# 普通python代码自上而下按照缩进执行，遇到错误就会停止后面的代码执行
# Person.eat()
zs.eat()
zs.sleep()
