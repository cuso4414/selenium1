import pytest
import time
from selenium_js.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=1000")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()
        time.sleep(3)
        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    @pytest.mark.skip
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)

    # @pytest.mark.skip
    def test_time(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.find_element_by_id("fromStationText").send_keys("西安")
        time.sleep(3)
        self.driver.find_element_by_id("toStationText").send_keys("宝鸡")
        # self.driver.find_element_by_id("train_date").send_keys("2020-12-30")
        # time.sleep(3)
        # self.driver.find_element_by_id("search_one").click()




