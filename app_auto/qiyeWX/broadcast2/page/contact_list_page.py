from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app_auto.qiyeWX.broadcast2.page.base_page import BasePage
from app_auto.qiyeWX.broadcast2.page.member_invite_page import MemberInviteMenuPage

# 通讯录列表页面
class ContactListPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_member(self):
        """
        添加成员
        :return:
        """
        # 滚动查找添加成员，并点击添加成员
        self.find_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)