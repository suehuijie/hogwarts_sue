from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMemberPage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def add_member_save(self):
        # input name
        # input account
        # input phone
        username = "sue-auto01"
        account = "20210204001"
        phonenum = "13474400001"
        sleep(5)
        self.driver.find_element(By.ID,'username').send_keys(username)
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys(account)
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys(phonenum)

        # 如果页面上相同属性的元素有多个，那么通过find_element定位到的元素是第一个
        self.driver.find_element_by_css_selector('.js_member_editor_form div:nth-child(3)>a:nth-child(2)').click()
        return True