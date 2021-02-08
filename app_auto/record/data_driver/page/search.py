from app_auto.record.data_driver.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._params["value"] = value
        self.steps("../page/search.yaml")