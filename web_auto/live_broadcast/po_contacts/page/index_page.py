from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from web_auto.live_broadcast.po_contacts.page.addmember_page import AddMemberPage


class IndexPage:

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = '127.0.0.1:9228'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def add_member_button(self):
        # sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)