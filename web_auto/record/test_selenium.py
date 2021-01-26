import selenium
from selenium import webdriver

def test_baidu():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")