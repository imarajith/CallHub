import pytest
import time
from selenium import webdriver
from PageObjects.PricingPage import PricingPage
from Utilities.CommonFunctions import Commons
from TestData import pricing

class TestYearly:

    def test_yearly_availability(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickYearlyPlan()
        self.driver.close()

    def test_yearly_business_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount=pricingPage.get_business_amount()
        expectedAmount=pricing.SubscriptionPricing["Yearly"]["Business"]["MonthAmount"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_yearly_business_billedamount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualBilledAmount=pricingPage.get_business_billedamount()
        expectedBilledAmount = pricing.SubscriptionPricing["Yearly"]["Business"]["BilledAmount"]["price"]
        Commons.assertValues(actualBilledAmount, expectedBilledAmount, self.driver)

    def test_yearly_premium_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount = pricingPage.get_premium_amount()
        expectedAmount = pricing.SubscriptionPricing["Yearly"]["Premium"]["MonthAmount"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_yearly_premium_billedamount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualBilledAmount = pricingPage.get_premium_billedamount()
        expectedBilledAmount = pricing.SubscriptionPricing["Yearly"]["Premium"]["BilledAmount"]["price"]
        Commons.assertValues(actualBilledAmount, expectedBilledAmount, self.driver)

    def test_yearly_payasugo_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount = pricingPage.get_payasugo_amount()
        expectedAmount = pricing.SubscriptionPricing["Yearly"]["Pay as you go"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_yearly_enterprise(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actual = pricingPage.get_custompricing()
        expected = pricing.SubscriptionPricing["Yearly"]["Enterprise"]
        Commons.assertValues(actual, expected, self.driver)





