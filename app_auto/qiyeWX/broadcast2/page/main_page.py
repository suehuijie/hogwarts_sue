from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app_auto.qiyeWX.broadcast2.page.base_page import BasePage
from app_auto.qiyeWX.broadcast2.page.contact_list_page import ContactListPage

# 主页
class MainPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def goto_contactlist(self):
        """
        进入到通讯录
        :return:
        """
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return ContactListPage(self.driver)