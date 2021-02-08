from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestLocator:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = "true"
        # desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = 'true'
        # 设置后可以输入中文字符
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1、 打开 雪球 app
        2、点击搜索输入框
        3、输入 阿里巴巴
        4、在搜索结果里面选择 ’阿里巴巴‘， 点击
        5、获取 阿里巴巴的股价，并判断 这只股价的价格 >200
        """
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price > 200

    def test_attr(self):
        """
        打开 雪球 应用首页
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入 alibaba
        判断 阿里巴巴 是否可见
        如果可见，打印 搜索成功， 否则 打印 搜索失败
        """
        element1 = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        print(element1.is_enabled())
        print(element1.text)
        print(element1.location)
        print(element1.size)
        if element1.is_enabled() == True:
            element1.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
            element2 = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            print(element2.get_attribute('displayed'))
            if element2.get_attribute('displayed') == 'true':
                print("搜索成功！")
            else:
                print("搜索失败！")


    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

    def test_get_currentprice(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        element = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = element.text
        assert float(current_price) > 200

    def test_myinfo(self):
        """
        1、点击我的，进入到个人信息页面
        2、点击登录，进入到登录页面
        3、输入用户名，输入密码
        4、点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('Qq123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

        # 找股票这个子节点的元素 （通过父节点找子节点）
        self.driver.find_element_by_android_uiautomator('new UiSelector().resoureId("com.xueqiu.android:id/title_container").childSelector(text("股票"))')
        # 通过相邻节点找兄弟节点

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true)'
                                                        '.instance(0)).scrollIntoView(new UiSelector()'
                                                        '.text("书剑笑傲").instance(0))').click()
        sleep(3)

if __name__=='__main__':
    pytest.main()