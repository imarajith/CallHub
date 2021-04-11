import pytest
import time
from selenium import webdriver
from PageObjects.PricingPage import PricingPage
from Utilities.CommonFunctions import Commons
from TestData import pricing

class TestMonthly:

    def test_monthly_availability(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickMonthlyPlan()
        self.driver.close()

    def test_monthly_business_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickMonthlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount=pricingPage.get_business_amount()
        expectedAmount=pricing.SubscriptionPricing["Monthly"]["Business"]["MonthAmount"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_monthly_business_billedamount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickMonthlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualBilledAmount=pricingPage.get_business_billedamount()
        expectedBilledAmount = pricing.SubscriptionPricing["Monthly"]["Business"]["BilledAmount"]["price"]
        Commons.assertValues(actualBilledAmount, expectedBilledAmount, self.driver)

    def test_monthly_premium_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickMonthlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount = pricingPage.get_premium_amount()
        expectedAmount = pricing.SubscriptionPricing["Monthly"]["Premium"]["MonthAmount"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_monthly_premium_billedamount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickMonthlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualBilledAmount = pricingPage.get_premium_billedamount()
        expectedBilledAmount = pricing.SubscriptionPricing["Monthly"]["Premium"]["BilledAmount"]["price"]
        Commons.assertValues(actualBilledAmount, expectedBilledAmount, self.driver)

    def test_monthly_payasugo_amount(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickMonthlyPlan()
        Commons.moveToPricingTable(self.driver)
        actualAmount = pricingPage.get_payasugo_amount()
        expectedAmount = pricing.SubscriptionPricing["Monthly"]["Pay as you go"]["price"]
        Commons.assertValues(actualAmount, expectedAmount, self.driver)

    def test_monthly_enterprise(self, setup):
        self.driver = setup
        Commons.get_url(self.driver)
        pricingPage = PricingPage(self.driver)
        pricingPage.clickMonthlyPlan()
        Commons.moveToPricingTable(self.driver)
        actual = pricingPage.get_custompricing()
        expected = pricing.SubscriptionPricing["Monthly"]["Enterprise"]
        Commons.assertValues(actual, expected, self.driver)





