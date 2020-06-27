from time import sleep

from selenium_frame_window.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("C:/Users/18729/PycharmProjects/fight/2/img/微信图片_20190814210757.jpg")
        sleep(3)