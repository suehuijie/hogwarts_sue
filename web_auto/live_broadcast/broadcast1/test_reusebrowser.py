import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        # 复用浏览器
        option = Options()
        # 注意 9223 端口要与命令行启用的端口保持一致  chrome --remote-debugging-port=9223
        option.debugger_address = "127.0.0.1:9223"
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        self.driver.quit()

    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#apps")
        self.driver.find_element(By.ID, 'menu_contacts').click()

