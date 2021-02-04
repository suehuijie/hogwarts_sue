from web_auto.live_broadcast.po_contacts.page.index_page import IndexPage


class TestContact:

    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        self.index.add_member_button().add_member_save()