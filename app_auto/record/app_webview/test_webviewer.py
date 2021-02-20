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
            "appPackage": "io.appium.android.apis",
            "appActivity": ".view.WebView1"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_webviewer(self):
        # self.driver.find_element(By.XPATH, '//*[@resource-id="i_am_a_textbox"]').send_keys('this is a test string')
        # sleep(3)
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'i am a link').click()
        # print(self.driver.page_source)

        # 因为原生页面和web页面的contexts 不一样，所以需要先跳转到web页面。类似切换frame
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, 'i_am_a_textbox').send_keys('this is a test string')
        self.driver.find_element(MobileBy.ID,'i am a link').click()
        print(self.driver.page_source)
