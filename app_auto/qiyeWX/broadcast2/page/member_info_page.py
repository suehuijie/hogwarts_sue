from appium.webdriver.common.mobileby import MobileBy
from app_auto.qiyeWX.broadcast2.page.base_page import BasePage
from app_auto.qiyeWX.broadcast2.page.modify_member_page import ModifyMember

# 个人信息页面
class MemberInfo(BasePage):
    def MemberInfo(self):
        """
        点击右上角三点符号，进入编辑成员页面
        :return:
        """
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iga"]').click()
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bct"]').click()
        return ModifyMember(self.driver)

