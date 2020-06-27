import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_weichat.page.base_page import BasePage


class Contact(BasePage):
    def get_member(self):
        '''
        得到所有的成员信息
        :return:
        '''
        # 这个列表存放所有的名单信息
        list = []
        while True:
            ele = (By.CSS_SELECTOR, ".ww_pageNav_info_text")
            self.waitfor_click(ele)
            # 获取翻页，message获取到的是一个1/3
            # 得到当前页和总页数，切割后是["1","3"]所以需要强转
            me: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            cur_page, total_page = [int(i) for i in me.split("/", 1)]
            member_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            # 把列表中的姓名拿出来
            for i in member_list:
                list.append(i.get_attribute("title"))
            # print(member_list) # return [member.get_attribute("title") for member in member_list]
            cur_page = [int(i) for i in me.split("/", 1)][0]
            if cur_page == total_page:
                print(list)
                return list
            self.find(By.CSS_SELECTOR, ".js_next_page").click()



            # for i in member_list:
            #     member=i.get_attribute("title")
            #     list.append(member)
            # print(list)
            # if cur_page == total_page:
            #     break
            # else:
            #     self.driver.find_element(By.CSS_SELECTOR,".ww_commonImg_PageNavArrowRightNormal").click()
