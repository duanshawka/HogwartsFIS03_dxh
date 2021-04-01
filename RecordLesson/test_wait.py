from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.liaoxuefeng.com/")
        # 隐式等待作为全局作用域，每次执行模块里面find方法的时候都会来执行，建议要用只能用一个比较短时间段的隐式等待，
        # 避免网络波动造成的未找到页面元素，不建议设置较长时间的隐式等待。建议多用显示等待
        self.driver.implicitly_wait(3)

    # def teardown(self):
    #     self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@href="/wiki/1016959663602400"]').click()
        # 以下为封装一个等待方法，等待某个元素在上面打开的页面存在，注意这个等待函数一定要有一个参数，比如x,下面until调用wait函数的时候，
        # 间接把前面WebDriverWait的self.driver参数传给了x，如果没有x就没有接餐对象
        # 还有个注意点：如果把一个函数当作一个参数传递，只用函数名，不能在函数名后加括号（），'函数名' 是参数，'函数名()'就变成调用了
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="uk-nav-header"]'))>=1
        # WebDriverWait(self.driver,10).until(wait)
        # 不封装就可以直接用expected_conditions
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="uk-nav-header"]')))

        self.driver.find_element(By.XPATH,'//*[@class="x-wiki-index-item"]').click()


