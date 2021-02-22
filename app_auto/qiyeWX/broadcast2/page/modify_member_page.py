from appium.webdriver.common.mobileby import MobileBy
from app_auto.qiyeWX.broadcast2.page.base_page import BasePage


class ModifyMember(BasePage):
    def delete_member(self):
        self.find_scroll("删除成员").click()
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bpc"]').click()
        # from app_auto.qiyeWX.broadcast2.page.search_member_page import SearchMember
        # return SearchMember(self.driver)

