import pytest
import time
from selenium import webdriver
from PageObjects.PricingPage import PricingPage
from Utilities.CommonFunctions import Commons
from TestData import pricing

class TestHalfYearly:

    def test_halfyearly_availability(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickHalfYearlyPlan()
        self.driver.close()

    def test_halfyearly_business_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickHalfYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount=pricingPage.get_business_amount()
        expectedAmount=pricing.SubscriptionPricing["Half Yearly"]["Business"]["MonthAmount"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_halfyearly_business_billedamount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickHalfYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualBilledAmount=pricingPage.get_business_billedamount()
        expectedBilledAmount = pricing.SubscriptionPricing["Half Yearly"]["Business"]["BilledAmount"]["price"]
        Commons.assertValues(actualBilledAmount, expectedBilledAmount, self.driver)

    def test_halfyearly_premium_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickHalfYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount = pricingPage.get_premium_amount()
        expectedAmount = pricing.SubscriptionPricing["Half Yearly"]["Premium"]["MonthAmount"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_halfyearly_premium_billedamount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickHalfYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualBilledAmount = pricingPage.get_premium_billedamount()
        expectedBilledAmount = pricing.SubscriptionPricing["Half Yearly"]["Premium"]["BilledAmount"]["price"]
        Commons.assertValues(actualBilledAmount, expectedBilledAmount, self.driver)

    def test_halfyearlyy_payasugo_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickHalfYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount = pricingPage.get_payasugo_amount()
        expectedAmount = pricing.SubscriptionPricing["Half Yearly"]["Pay as you go"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_halfyearly_enterprise(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickHalfYearlyPlan()
        Commons.moveToPricingTable(self.driver)
        actual = pricingPage.get_custompricing()
        expected = pricing.SubscriptionPricing["Half Yearly"]["Enterprise"]
        Commons.assertValues(actual, expected, self.driver)
