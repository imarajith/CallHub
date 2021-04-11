import pytest
import time
from selenium import webdriver
from PageObjects.PricingPage import PricingPage
from Utilities.CommonFunctions import Commons
from TestData import pricing

class TestQuaterly:

    def test_quaterly_availability(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickQuaterlyPlan()
        self.driver.close()

    def test_quaterly_business_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickQuaterlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount=pricingPage.get_business_amount()
        expectedAmount=pricing.SubscriptionPricing["Quaterly"]["Business"]["MonthAmount"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_quaterly_business_billedamount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickQuaterlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualBilledAmount=pricingPage.get_business_billedamount()
        expectedBilledAmount = pricing.SubscriptionPricing["Quaterly"]["Business"]["BilledAmount"]["price"]
        Commons.assertValues(actualBilledAmount, expectedBilledAmount, self.driver)

    def test_quaterly_premium_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickQuaterlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount = pricingPage.get_premium_amount()
        expectedAmount = pricing.SubscriptionPricing["Quaterly"]["Premium"]["MonthAmount"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_quaterly_premium_billedamount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickQuaterlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualBilledAmount = pricingPage.get_premium_billedamount()
        expectedBilledAmount = pricing.SubscriptionPricing["Quaterly"]["Premium"]["BilledAmount"]["price"]
        Commons.assertValues(actualBilledAmount, expectedBilledAmount, self.driver)

    def test_quaterly_payasugo_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickQuaterlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount = pricingPage.get_payasugo_amount()
        expectedAmount = pricing.SubscriptionPricing["Quaterly"]["Pay as you go"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_quaterly_enterprise(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickQuaterlyPlan()
        Commons.moveToPricingTable(self.driver)
        actual = pricingPage.get_custompricing()
        expected = pricing.SubscriptionPricing["Quaterly"]["Enterprise"]
        Commons.assertValues(actual, expected, self.driver)





