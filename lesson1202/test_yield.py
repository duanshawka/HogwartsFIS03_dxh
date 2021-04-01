import pytest


@pytest.fixture()
def login():
        username = 'xhduan'
        password = 'xhduan123'
        print("开始操作")
        # yield不仅是测试用例执行前/执行后的分解点，还可以返回值，如下列表或字典（相当于return），还可以记住上一次执行的位置
        # yield [username,password]
        yield {'username':username,'password':password}
        print("结束操作")

class TestDemo:
     def test_a(self,login):
         print(login)

