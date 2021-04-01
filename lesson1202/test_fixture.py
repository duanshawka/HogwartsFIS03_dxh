# def关键字定义的函数在类中的叫方法，在类外面的叫函数
# 通常执行用例前的一些前置工作放在@pytest.fixture()装置的方法里，最后放在conftest.py文件中，和逻辑代码分开，比如登陆，token获取

import pytest

# 单元测试框架 pytest 的 fixture定义：如下func_a()函数被定义为一个fixture的方法，可以被下面的测试用例调用
@pytest.fixture()
# 调用3：用autouse=True让文件中的所有测试用例都调用fixture方法（不建议使用），用这种调用方法，下面的测试用例传不传fixture方法名参数都可以
# @pytest.fixture(autouse=True)
def func_a():
    print("这是个用例执行前的fixture方法")

class TestDemo:
    # 调用1：测试用例中传入fixture方法名作为参数，即可在执行测试用例a前先执行fixture方法，作为用例的前置条件
    def test_a(self,func_a):
        print ("这是测试用例a")

    # 调用2：测试用例前添加如下装饰器，使用fixture方法名的字符串，即可在执行测试用例b前先执行fixture方法，作为用例的前置条件
    @pytest.mark.usefixtures("func_a")
    def test_b(self):
        print ("这是测试用例b")

    def test_c(self):
        print ("这是测试用例c")

