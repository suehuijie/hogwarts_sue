from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from web_auto.live_broadcast.po_contacts.page.addmember_page import AddMemberPage
from web_auto.live_broadcast.po_contacts.page.base_page import BasePage


class IndexPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def add_member_button(self):
        # sleep(3)
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)