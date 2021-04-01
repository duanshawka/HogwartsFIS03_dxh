import selenium
from selenium import webdriver

class TestIde:
    def setup(self):
        self.driver = webdriver.Chrome()
    def teardown(self):
        pass

    def test_ide(self):
