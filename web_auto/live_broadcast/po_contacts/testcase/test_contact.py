from web_auto.live_broadcast.po_contacts.page.index_page import IndexPage


class TestContact:

    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        username = "xixi-sue023"
        account = "202102040023"
        phonenum = "13474400023"
        addmemberpage = self.index.add_member_button()
        addmemberpage.add_member_save(username,account,phonenum)
        result = addmemberpage.get_member("sue-auto01")
        assert result
