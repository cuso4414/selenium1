from time import sleep

from selenium_frame_window.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("18710897621")
        sleep(2)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        # self.driver.switch_to.window(windows[1])
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("18729721769@163.com")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("18729721769")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)

