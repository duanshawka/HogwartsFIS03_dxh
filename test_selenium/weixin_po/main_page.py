from test_selenium.weixin_po.contact_page import ContactPage
from selenium import webdriver

class MainPage:
    def goto_contact_page(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')

        return ContactPage()
