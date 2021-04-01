import pytest

# fixture的params参数是一个列表，如果定义时传了params参数，在fixture方法中就要带上request参数
@pytest.fixture(params = ['a','b','c'])
def login(request):
    datas = request.param
    print("通过request.param 获取传入的参数")
    return datas

def test_case(login):
    # 通过打印 fixture方法名 获取fixture方法返回的数据
    # print(login)
    print("测试用例1")