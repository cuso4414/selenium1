import time

from selenium.webdriver.common.by import By
from test_weichat.page.add_member import AddMember
from test_weichat.page.base_page import BasePage


class Main(BasePage):
    def goto_add_member(self):
        # 点击跳转
        # time.sleep(3)
        # self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMember(self.driver)