import pytest
from selenium import webdriver
from Utilities.CommonFunctions import Commons
from Utilities.readProperties import ReadConfig

class TestPricing:

    # Verifies the page tile
    def test_PageTitle(self,setup):
        self.driver = setup
        Commons.get_url(self.driver)
        act_title=self.driver.title
        if act_title==ReadConfig.getPageTile():
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False


