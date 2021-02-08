from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestToast:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = '.view.PopupMenu1'
        # 不加也可以，因为默认就是uiautomator2
        desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Make a Popup!').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Search"]').click()
        # print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)