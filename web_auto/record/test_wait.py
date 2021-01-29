from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        # self.driver.implicitly_wait(3)

    def test_wait_1(self):
        self.driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]').click()
        sleep(5)
        self.driver.find_element_by_class_name('title_3p8-I').click()
        print("hello")

    def test_wait_2(self):
        self.driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]').click()
        self.driver.find_element_by_class_name('title_3p8-I').click()
        print("hello")

    def test_wait_3(self):
        self.driver.find_element_by_xpath('//*[@id="ember41"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="ember191"]/a/div/span').click()
        expected_conditions.element_to_be_clickable(By.XPATH, "xxxxxx")
        WebDriverWait(self.driver, 10).until()


    def teardown(self):
        self.driver.quit()
