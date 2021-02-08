import pytest as pytest
from appium import webdriver
from hamcrest import *

class TestGetAttr:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = "true"
        # desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = 'true'
        # 设置后可以输入中文字符
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_getattr(self):
        search_ele = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resourceId"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
        assert 'search' in search_ele.get_attribute("resourceId")

    def test_assert(self):
        a = 10
        b = 20
        assert a > b

    def test_hamcrest(self):
        # assert_that(10, equal_to(9), '这是一个提示')
        assert_that(8, close_to(10,2))
        assert_that("contains some string", contains_string("string"))