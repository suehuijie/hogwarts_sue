# app.py 存放app相关的操作，启动、关闭、进入到主页
from appium import webdriver

from app_auto.qiyeWX.broadcast2.page.base_page import BasePage
from app_auto.qiyeWX.broadcast2.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "sue"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            # caps["dontStopAppOnReset"] = "true"
            # 最重要的代码，建立客户端与服务端的连接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
            print("driver is None")
        else:
            print("driver is not None")
            # 启动app. 启用的页面时desirecaps里面设置的activity
            self.driver.launch_app()
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)