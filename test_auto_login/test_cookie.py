import os

import pytest
import time
from selenium import webdriver
import json

from selenium.webdriver.common.by import By


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/")

    @pytest.mark.skip
    def test_get_cookie(self):
        time.sleep(30)
        cookie = self.driver.get_cookies()
        # print(cookie)
        with open("cookie.json", "w") as f:
            # 将cookie存入一个json文件中
            json.dump(obj=cookie, fp=f)

    # 企业微信cookie有效期一天 中间扫过码cookie会失效
    def test_cookie_login(self):
        cookies = json.load(open("./cookie.json"))
        # 循环]cookies列表，将所有cookie添加到浏览器中
        for cookie in cookies:
            # 只添加一个cookie
            self.driver.add_cookie(cookie)
        time.sleep(2)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 打印当前文件路径,也是上传文件的路径
        dir = os.path.dirname(__file__)
        # 上传文件，上传文件可以使用send_keys。前提元素的标签必须为input。
        # send_keys里面放的文件,必须是绝对路径
        # dir = "C:/Users/18729/PycharmProjects/fight/test_auto_login"
        time.sleep(2)
        self.driver.find_element_by_id("js_upload_file_input").send_keys(dir+"/data.xlsx")
        ele_name = self.driver.find_element_by_id("upload_file_name").text
        # 断言上传文件名称
        assert ele_name == "data.xlsx"



