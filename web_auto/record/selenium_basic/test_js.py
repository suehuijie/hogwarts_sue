from time import sleep

import pytest as pytest

from web_auto.record.selenium_basic.base import Base


class TestJS(Base):

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        sleep(3)
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[2]/span[2]").click()
        sleep(3)
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))


    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        sleep(3)
        time_element = self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2021-02-05"')
        sleep(3)