from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.quit()