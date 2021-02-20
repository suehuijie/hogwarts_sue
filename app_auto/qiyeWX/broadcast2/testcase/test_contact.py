from app_auto.qiyeWX.broadcast2.page.app import App


class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = "hogwards_sue012"
        gender = "男"
        phone = '13800000012'

        result = self.main.goto_contactlist().add_member().add_member_manul().\
            edit_contact(name,gender,phone).verify_toast()
        assert result == '添加成功'

    def test_addcontact1(self):
        name = "hogwards_sue006"
        gender = "男"
        phone = '13800000006'

        result = self.main.goto_contactlist().add_member().add_member_manul().\
            edit_contact(name,gender,phone).verify_toast()
        assert result == '添加成功'

    def teardown_class(self):
        self.app.stop()