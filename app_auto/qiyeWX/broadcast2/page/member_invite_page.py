from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app_auto.qiyeWX.broadcast2.page.base_page import BasePage
from app_auto.qiyeWX.broadcast2.page.contact_add_page import ContactAddPage

# 添加成员方式页面
class MemberInviteMenuPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_member_manul(self):
        """
        进入手动编辑成员页面
        :return:
        """
        # 点击手动输入添加
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ContactAddPage(self.driver)

    def verify_toast(self):
        result = self.get_toast_text()
        return result