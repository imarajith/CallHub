from selenium import webdriver
from readProperties import ReadConfig
import time

class Commons:

    @staticmethod
    def get_url(driver):
        driver.get(ReadConfig.getApplicationURL())
        time.sleep(5)

    @staticmethod
    def moveToPricingTable(driver):
        element = driver.find_element_by_xpath("//*[@id='planpricetab']")
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def assertValues(actual, expected, driver):
        if actual==expected:
            driver.close()
            assert True
        else:
            driver.close()
            assert False
