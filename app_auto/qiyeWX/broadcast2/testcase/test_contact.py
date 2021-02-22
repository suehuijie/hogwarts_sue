from app_auto.qiyeWX.broadcast2.page.app import App


class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()
        self.name = "hogwards_sue013"
        self.gender = "男"
        self.phone = '13800000013'


    def test_addcontact(self):
        result = self.main.goto_contactlist().add_member().add_member_manul().\
            edit_contact(self.name,self.gender,self.phone).verify_toast()
        assert result == '添加成功'

    def test_delcontact(self):
        result = self.main.goto_contactlist().search_button().search_member(self.name).\
            MemberInfo().delete_member()



    def teardown_class(self):
        self.app.stop()