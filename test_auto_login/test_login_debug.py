from time import sleep
from selenium import webdriver
# 小写的chrome
from selenium.webdriver.chrome.options import Options

class TestLogin:
    def test_debug_login(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        driver = webdriver.Chrome(r'C:\myTestTool\chromedriver\chromedriver.exe', options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")


