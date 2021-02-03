from time import sleep

from selenium import webdriver


class TestDemo():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_wx(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)