from time import sleep

from web_auto.record.selenium_basic.base import Base


class TestFile(Base):

    def test_file_upload(self):
        self.driver.get("http://www.baidu.com/")
        self.driver.find_element_by_xpath('//*[@class="soutu-btn"]').click()
        self.driver.find_element_by_xpath('//*[@class="upload-pic"]').send_keys('F:\重要\hogwarts_sue\\resource\photo1.jpg')
        sleep(3)