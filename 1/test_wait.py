from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        # 隐式等待
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        # 强制等待3秒
        # sleep(3)
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        print("hello")
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*["@calss="table-heading"]')) >= 1
        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()


