from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Locators import Locators


class SignOn:

    def __init__(self, driver):
        self.driver = driver

        self.home = Locators.homelink
        self.loginUserName_xpath = Locators.loginUserName_xpath
        self.loginPassword_xpath = Locators.loginPassword_xpath
        self.loginSubmit_xpath = Locators.loginSubmit_xpath

    def click_home(self):
        self.driver.find_element(By.XPATH, self.home).click()

    def login_user(self, username, password):
        self.driver.find_element(By.XPATH, self.loginUserName_xpath).clear()
        self.driver.find_element(By.XPATH, self.loginUserName_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.loginPassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.loginPassword_xpath).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.loginSubmit_xpath).click()
