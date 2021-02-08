from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
import pytest

class TestParam:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = True
        # 设置后可以输入中文字符
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize('searchkey, type, price',[
        ('alibaba', 'BABA', 280),
        ('xiaomi', '01810', 30)
    ])
    def test_search(self, searchkey, type, price):
        print("搜索测试用例")
        """
        1、 打开 雪球 app
        2、点击搜索输入框
        3、输入 搜索词：阿里巴巴、小米 等等
        4、在搜索结果里面点击第一个搜索结果
        5、判断 这只股价的价格 >200
        """
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name"]').click()
        current_price = self.driver.find_element(MobileBy.XPATH, f'//*[@text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        expecte_price = price
        assert_that(float(current_price), close_to(expecte_price, expecte_price*0.2))