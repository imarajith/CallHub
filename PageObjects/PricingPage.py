from selenium import webdriver

class PricingPage:
    monthly_plan_xpath="//h6[contains(text(), 'Monthly')]"
    quaterly_plan_xpath = "//h6[contains(text(), 'Quarterly')]"
    half_yearly_plan_xpath = "//h6[contains(text(), 'Half-yearly')]"
    yearly_plan_xpath = "//h6[contains(text(), 'Yearly')]"

    business_amount_xpath = "//h5[contains(text(),'Business')]/preceding-sibling::div/h3"
    business_billedamount_xpath = "//h5[contains(text(),'Business')]/preceding-sibling::div/small"
    premium_amount_xpath = "//h5[contains(text(),'Premium')]/preceding-sibling::div/h3"
    premium_billedamount_xpath = "//h5[contains(text(),'Premium')]/preceding-sibling::div/small"
    payasugo_amount_xpath = "//h5[contains(text(),'Pay as you go')]/preceding-sibling::div/h3"
    enterprice_xpath="//div[contains(@class,'enterprise-container text-center ')]/following-sibling::p"

    def __init__(self, driver):
        self.driver = driver

    def clickMonthlyPlan(self):
        self.driver.find_element_by_xpath(self.monthly_plan_xpath).click()

    def clickQuaterlyPlan(self):
        self.driver.find_element_by_xpath(self.quaterly_plan_xpath).click()

    def clickHalfYearlyPlan(self):
        self.driver.find_element_by_xpath(self.half_yearly_plan_xpath).click()

    def clickYearlyPlan(self):
        self.driver.find_element_by_xpath(self.yearly_plan_xpath).click()

    def get_business_amount(self):
        value=self.driver.find_element_by_xpath(self.business_amount_xpath).text
        return value.strip()

    def get_business_billedamount(self):
        value=self.driver.find_element_by_xpath(self.business_billedamount_xpath).text
        return value.strip()

    def get_premium_amount(self):
        value=self.driver.find_element_by_xpath(self.premium_amount_xpath).text
        return value.strip()

    def get_premium_billedamount(self):
        value=self.driver.find_element_by_xpath(self.premium_billedamount_xpath).text
        return value.strip()

    def get_payasugo_amount(self):
        value=self.driver.find_element_by_xpath(self.payasugo_amount_xpath).text
        return value.strip()

    def get_custompricing(self):
        value = self.driver.find_element_by_xpath(self.enterprice_xpath).text
        return value.strip()

