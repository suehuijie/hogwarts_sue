from app_auto.record.data_driver.page.base_page import BasePage
from app_auto.record.data_driver.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)