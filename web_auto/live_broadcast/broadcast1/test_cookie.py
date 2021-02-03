import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        # 添加cookie后可以用这个
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850055710825'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'AhFC2QyR-u5Q_yfJ5uZD183xzLevHHL0KJcU_NJ5_i8dRqgUtQY7duh-I01jqKR7'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4050242'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324951186110'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850055710825'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612343551'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2866071665751346'}, {'domain': '.qq.com', 'expiry': 1612427145, 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False, 'value': '1612340745110'}, {'domain': '.qq.com', 'expiry': 1612430573, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1326192419.1612333695'}, {'domain': 'work.weixin.qq.com', 'expiry': 1612365229, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5hbn0hu'}, {'domain': '.qq.com', 'expiry': 1675416173, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.740896388.1612333695'}, {'domain': '.work.weixin.qq.com', 'expiry': 1643869693, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '6kWNl-X-P1Siri2nb3ayrOua1ifmOaBUysw6MPt1uORqjnuF36EKGALwdwJgQS7GkASmExvCnvR0NltcesCuJrCTtsnqXaHo1O_gcrty-WwaphXfo_weJH6CxvQ--JGhJjDDMt2JkUdaICVSFd7FAp0lYgw4W-LrVkWOAaEtA017GqJkizQGG3k5RrHHrbv3rIf6hhWXNeml3PxUneAZppX-48YWPnl95GLF692F4tvqoe7LRYNthRyNHx8x10qIsEsz1dOp2EqEd-kF4tOaUw'}, {'domain': '.qq.com', 'expiry': 1614500130, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o1063514310'}, {'domain': '.qq.com', 'expiry': 1614500130, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000960e741dffed132f75b1900e471ad0bbda73777ee783cd106290136178e0521168fe54b1b8b784c9'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'iZ4ZuwRvW9'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'f65107d378412d174f47e207275d5449278a88ef63afa66b9ee5b1ded5de42ba'}, {'domain': '.qq.com', 'expiry': 1927091264, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_b819a18d256b0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1614936176, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1643879551, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612333694,1612343123,1612343551'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '2281041168'}]

        print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def test_db(self):
        # 添加cookies到数据库中
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850055710825'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'AhFC2QyR-u5Q_yfJ5uZD183xzLevHHL0KJcU_NJ5_i8dRqgUtQY7duh-I01jqKR7'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4050242'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324951186110'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850055710825'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612343551'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2866071665751346'}, {'domain': '.qq.com', 'expiry': 1612427145, 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False, 'value': '1612340745110'}, {'domain': '.qq.com', 'expiry': 1612430573, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1326192419.1612333695'}, {'domain': 'work.weixin.qq.com', 'expiry': 1612365229, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5hbn0hu'}, {'domain': '.qq.com', 'expiry': 1675416173, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.740896388.1612333695'}, {'domain': '.work.weixin.qq.com', 'expiry': 1643869693, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '6kWNl-X-P1Siri2nb3ayrOua1ifmOaBUysw6MPt1uORqjnuF36EKGALwdwJgQS7GkASmExvCnvR0NltcesCuJrCTtsnqXaHo1O_gcrty-WwaphXfo_weJH6CxvQ--JGhJjDDMt2JkUdaICVSFd7FAp0lYgw4W-LrVkWOAaEtA017GqJkizQGG3k5RrHHrbv3rIf6hhWXNeml3PxUneAZppX-48YWPnl95GLF692F4tvqoe7LRYNthRyNHx8x10qIsEsz1dOp2EqEd-kF4tOaUw'}, {'domain': '.qq.com', 'expiry': 1614500130, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o1063514310'}, {'domain': '.qq.com', 'expiry': 1614500130, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000960e741dffed132f75b1900e471ad0bbda73777ee783cd106290136178e0521168fe54b1b8b784c9'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'iZ4ZuwRvW9'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'f65107d378412d174f47e207275d5449278a88ef63afa66b9ee5b1ded5de42ba'}, {'domain': '.qq.com', 'expiry': 1927091264, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_b819a18d256b0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1614936176, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1643879551, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612333694,1612343123,1612343551'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '2281041168'}]
        # shelve 模块， python 自带的对象持久化存储
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()


    def test_import_contact(self):
        # 从数据库中取数据
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()

        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 假如cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 批量导入联系人
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element_by_id('js_upload_file_input').send_keys("E:\前端培训 -- Jira使用手册V2.0_20190308(1).xlsx")
        result = self.driver.find_element_by_id('upload_file_name').text

        # 判断上传名与实际上传名一致
        assert "前端培训 -- Jira使用手册V2.0_20190308(1).xlsx" == result
        sleep(5)