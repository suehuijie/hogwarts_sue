from selenium.webdriver.remote.webdriver import WebDriver

# 存放driver的初始化，或者存放一些基本的方法，find、get_toast
class BasePage:
    def __init__(self,driver:WebDriver = None):
        self.driver = driver

## __init__(self) 类的构造方法 （构造类的实例，会先执行该方法）
## setup() 资源的初始化