import os

from selenium import webdriver


class Base():

    # # 多浏览器运行测试用例，可通过传入的参数确定是哪个浏览器执行
    # def setup(self):
    #     browser = os.getenv("browser")
    #     if browser == 'firefox':
    #         self.driver = webdriver.Firefox()
    #     elif browser == 'headless':
    #         self.driver = webdriver.PhantomJS()
    #     else:
    #         self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(3)

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()