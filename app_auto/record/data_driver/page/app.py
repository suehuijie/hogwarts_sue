from appium import webdriver
from app_auto.record.data_driver.page.base_page import BasePage
from app_auto.record.data_driver.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver == None:
            desire_cap = {
                "platformName": "android",
                "deviceName": "sue",
                "appPackage": _package,
                "appActivity": _activity,
                "autoGrantPermissions": True
            }
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(_package)

        return self

    def main(self):
        return Main(self._driver)