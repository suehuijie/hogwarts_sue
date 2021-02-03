import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwards():

    # 初始化环境
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待，加载出来后再操作
        self.driver.implicitly_wait(5)

    # 清理环境，资源回收
    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        # time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "求职面试圈").click()
        # time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".topic-27641 .title > a").click()
        # time.sleep(2)
