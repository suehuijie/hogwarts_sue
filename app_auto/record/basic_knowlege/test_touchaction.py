from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
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

    def test_touchaction(self):
        # self.driver.find_element_by_id()
        action = TouchAction(self.driver)
        action.press(x=160,y=235).move_to(x=477,y=235).wait(200).move_to(x=800,y=235).wait(200).move_to(x=800,y=553).wait(200)\
            .move_to(x=800,y=876).release().perform()