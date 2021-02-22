from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app_auto.qiyeWX.broadcast2.page.base_page import BasePage
from app_auto.qiyeWX.broadcast2.page.member_invite_page import MemberInviteMenuPage

# 通讯录列表页面
from app_auto.qiyeWX.broadcast2.page.search_member_page import SearchMember


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

    def search_button(self):
        """
        点击搜索成员图标，进入搜索成员页面
        :return:
        """
        self.find(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView').click()
        return SearchMember(self.driver)