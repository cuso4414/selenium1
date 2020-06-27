import time
from selenium.webdriver.common.by import By
from test_weichat.page.base_page import BasePage
from test_weichat.page.contact import Contact

class AddMember(BasePage):

    _ele_username = "username"

    def add_member(self):
        # time.sleep(3)
        self.find(By.ID, self._ele_username).send_keys("庄周")

        self.find(By.ID, "memberAdd_acctid").send_keys("900184")

        self.find(By.ID, "memberAdd_phone").send_keys("11122223334")

        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # # 姓名
        # self.driver.find_element_by_id("username").send_keys("庄周")
        # # 账号
        # self.driver.find_element_by_id("memberAdd_acctid").send_keys("900184")
        # # 手机号
        # self.driver.find_element_by_id("memberAdd_phone").send_keys("11122223334")
        # # 点击保存
        # self.driver.find_element_by_css_selector(".js_btn_save").click()
        return Contact(self.driver)

    def add_member_fail(self):
        time.sleep(10)
        # 姓名
        self.find(By.ID, "username").send_keys("阿英")
        # 账号
        self.find(By.ID, "memberAdd_acctid").send_keys("900184")
        # 手机号
        self.find(By.ID, "memberAdd_phone").send_keys("11122223334")
        # 点击保存
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self.driver)