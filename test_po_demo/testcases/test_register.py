from test_po_demo.page.test_page import IndexPage


class TestRegister:
    def test_login_register(self):
        index = IndexPage()
        # 点击进入登陆页面,点击立即注册,进入注册页面,开始注册
        index.goto_login().goto_register().register()

        