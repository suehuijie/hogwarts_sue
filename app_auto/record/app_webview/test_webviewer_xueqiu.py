from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestBrowser:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "platformVersion": "6.0",
            # "browserName": 'Browser',
            "noReset": True,
            "deviceName": 'sue',
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_webviewer_xueqiu(self):
        # 点击交易
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        # 切换上下文
        print(self.driver.contexts)
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.window_handles)
        A_locator = (MobileBy.XPATH,'//android.view.View[@content-desc="A股开户"]')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        # print(self.driver.window_handles)
        # self.driver.switch_to.window()
        print(self.driver.contexts)

        # # 显示等待
        phonenumber_locator = (MobileBy.ID, 'phone-number')
        WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable(phonenumber_locator))
        #
        # # 输入用户名和验证码，点击立即开户
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(phonenumber_locator).send_keys('18509251760')
        self.driver.find_element(MobileBy.ID, 'code').send_keys('1234')
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'立即开户').click()