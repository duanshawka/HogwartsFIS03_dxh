from test_selenium.weixin_po.main_page import MainPage


class TestLogin:
    def setup(self):
        self.main = MainPage()


    def teardown(self):
        pass

    def test_login(self):
        name = 'wahaha1'
        id = 'wahaha1'
        mail = 'wahaha1@qq.com'
        namevalue = self.main.goto_contact_page().click_add_member()\
            .add_member_page(name,id,mail).get_member()
        assert name in namevalue
        print(namevalue)