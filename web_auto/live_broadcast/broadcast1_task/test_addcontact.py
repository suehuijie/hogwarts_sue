import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestContact:

    def setup(self):
        # # 复用浏览器的时候使用下面的代码
        # option = webdriver.ChromeOptions()
        # option.debugger_address = '127.0.0.1:9224'
        # self.driver = webdriver.Chrome(options=option)

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 通过复用浏览器获取到cookie
    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = self.driver.get_cookies()
        print(cookies)

    # 将cookie保存到数据库中
    def test_save_cookie(self):
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850055710825'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '5cepHf3bLaXeH5MWB6Ov_BOxJDVg6B4AHTe0S23qjZHk6JT8s6nrqvSBbT-VgJSLiAv8AAORGQ-u5VkwhSJphwNwcsFtQNE4Cc31SoHXE41-VDh7xErA3RRf8iNLkmYwFbzK0tG9FTP9mqwVCiv4bn28zwild7BbKXCgDfcXiYcFqVIdmGiCAD-WPpNgsjQ4lMUAW78SRpodvpbUr6zzUsp7fDf8Jy55cR1v6kdLy4hk6HQhLS8N1KRxhNGT8Vz75LYT2Mj2zKHSgkcnoVJhiw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'AhFC2QyR-u5Q_yfJ5uZD140jj9ncR-aQDzxUO4PtMl8aPWJZakaXxa1xC5CFMJPX'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8513435'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324951186110'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850055710825'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1643944247, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612343123,1612343551,1612404345,1612408247'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612408247'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2866071665647712'}, {'domain': '.qq.com', 'expiry': 1612494659, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1326192419.1612333695'}, {'domain': 'work.weixin.qq.com', 'expiry': 1612435620, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'innfr9'}, {'domain': '.qq.com', 'expiry': 1612408307, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1643942688, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1675480259, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.740896388.1612333695'}, {'domain': '.work.weixin.qq.com', 'expiry': 1615000262, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]

        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()

        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()

    def test_add_contact(self):
        # 从数据库中取出cookie
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()

        # 打开无痕新页面, 添加cookie后刷新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(3)
        # 添加联系人
        self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1)>div:nth-child(1)+a').click()
        sleep(3)
        self.driver.find_element_by_id('username').send_keys('宋会洁-自动化02')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('20101120302')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('18509251762')
        self.driver.find_element_by_css_selector('.js_member_editor_form div:nth-child(3)>a:nth-child(2)').click()
        sleep(3)

        # 添加断言，判断添加联系人是否成功
        user_name = self.driver.find_element_by_css_selector('#member_list>tr:nth-last-child(1)>td:nth-child(2)>span').text
        print(user_name)
        assert user_name == "宋会洁-自动化02"