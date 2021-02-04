from web_auto.live_broadcast.po_demo.page.main_page import MainPage


class TestRegister:

    def setup(self):
        self.main = MainPage()

    def test_register(self):
        result = self.main.goto_login().goto_regsiter().register()
        # self.main.goto_register().register()
        assert result