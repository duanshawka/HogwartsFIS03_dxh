from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_selenium.weixin_po.add_member_page import AddMemberPage
from selenium import webdriver

class ContactPage:
    def click_add_member(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)

        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(ele))
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

        return AddMemberPage()


    def get_member(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)

        # 开始get_member方法中没有复用浏览器的代码，在上面下面的driver前加self，用例执行报错，但是数据插入了？
        # 想的是一个模块里面上面的方法click_add_member已经复用浏览器了，每个方法都要初始化浏览器？
        name_ele = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_value = []
        # 遍历数组，取出其属性title的值，存入name_value中
        for value in name_ele:
            print(value.get_attribute("title"))
            name_value.append(value.get_attribute("title"))
        return name_value
