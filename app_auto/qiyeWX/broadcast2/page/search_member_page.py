from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from app_auto.qiyeWX.broadcast2.page.base_page import BasePage
from app_auto.qiyeWX.broadcast2.page.member_info_page import MemberInfo

# 搜索成员页面
class SearchMember(BasePage):
    def search_member(self,contactname):
        """
        输入要搜索的成员姓名，自动返回搜索结果
        :param contactname:
        :return:
        """
        self.find(MobileBy.XPATH,'//*[@text="搜索"]').send_keys(contactname)
        sleep(2)
        search_result = self.driver.find_elements(MobileBy.XPATH,f'//*[@text="{contactname}"]')
        sleep(2)
        result_length = len(search_result)
        print(result_length)
        if result_length < 2:
            print("查找结果为空")
        else:
            del_element = search_result[1]
            del_element.click()
            return MemberInfo(self.driver)