from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_auto.live_broadcast.po_contacts.page.base_page import BasePage


class AddMemberPage(BasePage):

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def add_member_save(self,username,account,phonenum):
        # input name
        # input account
        # input phone
        # username = "aa-sue01"
        # account = "20210204001"
        # phonenum = "13474400001"
        # sleep(5)
        self.find(By.ID,'username').send_keys(username)
        self.find(By.ID,'memberAdd_acctid').send_keys(account)
        self.find(By.ID,'memberAdd_phone').send_keys(phonenum)

        # 如果页面上相同属性的元素有多个，那么通过find_element定位到的元素是第一个
        self.find(By.CSS_SELECTOR,'.js_member_editor_form div:nth-child(3)>a:nth-child(2)').click()
        return True

    def get_member(self,value):
        locator = (By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_for_click(locator)
        # sleep(2)
        # find_elements 方法返回的是元素列表【element1，element2....】
        # elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td')
        # 这段也可以用，下面一条代码是这三行的列表推导式
        # titles = [element.get_attribute("title") for element in elements]

        titles_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td')
            titles = [element.get_attribute("title") for element in elements]
            if value in titles:
                return True
            titles_total.extend(titles)

            page:str = self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            num,total = page.split("/",1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR,'.ww_pageNav_info a:nth-last-child(1)').click()

        return titles_total
