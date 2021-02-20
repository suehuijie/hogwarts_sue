from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    name = "hogwards_sue002"
    gender = "男"
    phone = '13800000002'

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "sue"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps["dontStopAppOnReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_contact(self):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0))').click()

        # 添加联系人
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(self.name)
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        if self.gender == "男":
            self.driver.find_element(MobileBy.XPATH,'//*[@text="男"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手机号"]').send_keys(self.phone)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("保存").instance(0))').click()
        sleep(2)
        print(self.driver.page_source)

        # 断言是否添加成功
        message = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
        assert message == "添加成功"

        # 返回到首页
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/ibz"]/../../android.widget.TextView').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="消息"]').click()

    def test_del_contact(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="搜索"]').send_keys(self.name)
        sleep(3)
        search_result = self.driver.find_elements(MobileBy.XPATH,f'//*[@text="{self.name}"]')
        length = len(search_result)
        # print(length)
        del_element = search_result[1]
        if length >= 2:
            del_element.click()
            self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/igo"]').click()
            self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/bct"]').click()
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector()'
                                     '.scrollable(true).instance(0))'
                                     '.scrollIntoView(new UiSelector()'
                                     '.text("删除成员").instance(0))').click()
            self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/bpc"]').click()

            # 断言删除成功
            # self.driver.refresh()
            sleep(2)
            latest_search_result = self.driver.find_elements(MobileBy.XPATH,f'//*[@text="{self.name}"]')
            latest_length = len(latest_search_result)
            assert latest_length == length - 1
        else:
            print("查找结果为空")
