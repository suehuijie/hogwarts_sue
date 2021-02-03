from web_auto.record.pageobject import Main


class TestRegister:

    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()