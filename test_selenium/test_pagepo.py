"""
此模块为页面用例不分离的硬编码，要实现以下优化：
1/按照页面分模块，把每个页面涉及到的功能写成方法
2/公共的代码比如 driver初始化要单独封装，用于被继承
3/写入的数据要参数化，这里主要是add_member_page页面的add_member_page(self)方法

"""

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddContacts:
    # def setup(self):
    #     opt = webdriver.ChromeOptions()
    #     opt.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=opt)
    #     self.driver.implicitly_wait(10)


    def test_addcontacts(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        #   不明白上面的隐式等待对于下面找"添加成员"不生效,要添加下面显示等待 等待元素出现
        ele = (By.CSS_SELECTOR,".ww_operationBar .js_add_member")
        WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(ele))
        while True:
            # ele = self.driver.find_element_by_css_selector(".ww_operationBar .js_add_member")
            # ele.click()
            # ele为数组，*ele代表解数组
            driver.find_element(*ele).click()
            # 以下使用find_element_by_id 找到的元素是一个字符串
            # element = driver.find_element_by_id("username")
            element = driver.find_elements_by_id("username")
            if len(element) > 0:
                break
        driver.find_element_by_id("username").send_keys("wahaha2")
        driver.find_element_by_id("memberAdd_acctid").send_keys("wahaha2")
        driver.find_element_by_id("memberAdd_mail").send_keys("wahaha2@qq.com")
        driver.find_element_by_css_selector(".ww_operationBar .js_btn_save").click()
        # self.driver.find_element_by_css_selector(".js_btn_save").click()
        # 得到关于姓名的数组names
        name_ele = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_value = []
        # 遍历数组，取出其属性title的值，存入name_value中
        for value in name_ele:
            print(value.get_attribute("title"))
            name_value.append(value.get_attribute("title"))
        assert "wahaha2" in name_value
        print(name_value)


