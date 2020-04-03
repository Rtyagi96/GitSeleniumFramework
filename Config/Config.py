from idlelib.multicall import r
import pytest
import json
from selenium import webdriver
import os

class ReadJson:

    def __init__(self):
        self.browser = td.testData("browser")
        self.baseUrl = td.testData("environment")

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        :return 'WebDriver Instance':
        """

        if self.browser == "firefox":
            driver = webdriver.Firefox()

        elif self.browser == "chrome":
            # Set Chrome driver
            driverLocation = "C:/Users/Rohit/PycharmProjects/SeleniumFramework/drivers/chromedriver_win32/chromedriver.exe"
            driver = webdriver.Chrome(driverLocation)
            driver.maximize_window()

        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(15)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.environment)

        return driver


def readJson(testDataPath):
    return None