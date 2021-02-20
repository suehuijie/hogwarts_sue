# from app_auto.qiyeWX.broadcast2.page.member_invite_page import MemberInviteMenuPage

# 编辑成员页面
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app_auto.qiyeWX.broadcast2.page.base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def edit_contact(self,name,gender,phone):
        """
        编辑成员信息
        :return:
        """
        # 输入姓名、性别、手机号并点击保存
        self.find(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        self.find(MobileBy.XPATH,'//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        if gender == "男":
            self.find(MobileBy.XPATH,'//*[@text="男"]').click()
        else:
            self.find(MobileBy.XPATH,'//*[@text="女"]').click()
        self.find(MobileBy.XPATH,'//*[@text="手机号"]').send_keys(phone)
        self.find_scroll("保存").click()
        sleep(2)
        print(self.driver.page_source)

        from app_auto.qiyeWX.broadcast2.page.member_invite_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)