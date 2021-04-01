# test_calcu.py 用于存放测试用例

from business_code.calcu import Calculator

class TestCalc:
    # 类中的每个测试方法都去实例化一个类，可以抽离出来做成类级别的setup方法
    def setup_class(self):
        # 如果calc不加self就是普通类变量，后面的测试用例就引用不了，加上self后 self.calc就变成实例变量，也就是全局变量，作用域扩大
        self.calc = Calculator()
    def test_add1(self):
        # 在一个测试类的测试方法里实例化另一个类，然后通过该实例调用另一个类里的某个方法（加法业务逻辑）
        # calc = Calculator()
        result = self.calc.add(1,2)
        assert result == 3
    # 同一个类下面的方法名不能重名，不同方法下的变量是可以同名的，因为非全局变量，即使同名也代表不同的变量。
    def test_add2(self):
        cal = Calculator()
        result = self.calc.add(0.1,0.2)
        assert round(result,2) == 0.3

    def test_add3(self):
        cal = Calculator()
        result = self.calc.add(-1,-2)
        assert result == -3