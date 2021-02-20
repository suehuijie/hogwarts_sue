import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

# 存放driver的初始化，或者存放一些基本的方法，find、get_toast
class BasePage:
    ## __init__(self) 类的构造方法 （构造类的实例，会先执行该方法）
    ## setup() 资源的初始化

    # 在logging.basicConfig前清理已有 handlers
    root_logger = logging.getLogger()
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%m:%S',
                        filename= '../log/myapp.log',
                        filemode='w')
    def __init__(self,driver:WebDriver = None):
        self.driver = driver

    def find(self,by,locator):
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by,locator)

    def find_scroll(self,text):
        logging.info("find by scroll")
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector()'
                  '.scrollable(true).instance(0))'
                  '.scrollIntoView(new UiSelector()'
                  f'.text("{text}").instance(0))')

    def get_toast_text(self):
        logging.info("get toast:")
        result = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
        logging.info(result)
        return result
