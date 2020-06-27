from test_weichat.page.base_page import BasePage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestApple:
    def setup(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(r'C:\myTestTool\chromedriver\chromedriver.exe', options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    def test_apple(self):
        me: str = self.driver.find_element_by_css_selector(".ww_pageNav_info_text").text
        print('me', me)
        cur_page, total_page = [int(i) for i in me.split("/", 1)]
        print("cur_page", cur_page)
        print("total_page", total_page)


