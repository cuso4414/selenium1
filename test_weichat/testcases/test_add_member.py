import pytest
from test_weichat.page.main import Main

class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        assert "庄周" in self.main.goto_add_member().add_member().get_member()

    @pytest.mark.skip
    def test_add_member_fail(self):
        main = Main()
        assert "阿香" not in main.goto_add_member().add_member_fail().get_member()

    def teardown(self):
        self.main.quit()
'''
[<selenium.webdriver.remote.webelement.WebElement (session="689efbbc3906a046e7848bb75d144400", element="ebd83cc8-edaa-4dca-99d8-61670d909424")>, <selenium.webdriver.remote.webelement.WebElement (session="689efbbc3906a046e7848bb75d144400", element="4032f233-770a-4a68-9873-49691b53de16")>, <selenium.webdriver.remote.webelement.WebElement (session="689efbbc3906a046e7848bb75d144400", element="eb8987da-2742-4230-9e48-9bfd2da3e2e0")>]
'''

