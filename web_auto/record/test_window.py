from time import sleep

from selenium import webdriver
from web_auto.record.base import Base

class TestFrame(Base):

    def test_window(self):
        self.driver.get("http://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("18509251760")
        sleep(3)
        self.driver.switch_to.window(windows[0])
        sleep(2)
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("sue")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("password")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)