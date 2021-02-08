from app_auto.record.data_driver.page.base_page import BasePage
from app_auto.record.data_driver.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)