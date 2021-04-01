import time

from selenium import webdriver


class AddMemberPage:
    def add_member_page(sel,name,id,mail):
        from test_selenium.weixin_po.contact_page import ContactPage

        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)

        time.sleep(2)
        driver.find_element_by_id("username").send_keys(name)
        driver.find_element_by_id("memberAdd_acctid").send_keys(id)
        driver.find_element_by_id("memberAdd_mail").send_keys(mail)
        driver.find_element_by_css_selector(".ww_operationBar .js_btn_save").click()

        return ContactPage()
