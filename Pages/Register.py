from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Locators import Locators


class RegisterUser(object):

    def __init__(self, driver):
        self.driver = driver

        #  Contact Information
        self.register_xpath = Locators.register_xpath
        self.firstName_xpath = Locators.firstName_xpath
        self.lastName_xpath = Locators.lastName_xpath
        self.phone_xpath = Locators.phone_xpath
        self.email_xpath = Locators.email_xpath

        #  Mailing Information
        self.address_xpath = Locators.address_xpath
        self.city_xpath = Locators.city_xpath
        self.state_xpath = Locators.state_xpath
        self.postalCode_xpath = Locators.postalCode_xpath

        #  User Information
        self.userName_xpath = Locators.userName_xpath
        self.password_xpath = Locators.password_xpath
        self.confirmPassword_xpath = Locators.confirmPassword_xpath
        self.submitButton_xpath = Locators.submitButton_xpath
        self.registerText_xpath = Locators.registerText_xpath

    def contact_information(self, fname, lname, phone, email):
        self.driver.find_element(By.XPATH, self.register_xpath).click()
        self.driver.find_element(By.XPATH, self.firstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstName_xpath).send_keys(fname)
        self.driver.find_element(By.XPATH, self.lastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastName_xpath).send_keys(lname)
        self.driver.find_element(By.XPATH, self.phone_xpath).send_keys(phone)
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def mailing_information(self, address, city, state, postalCode):
        self.driver.find_element(By.XPATH, self.address_xpath).send_keys(address)
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.state_xpath).send_keys(state)
        self.driver.find_element(By.XPATH, self.postalCode_xpath).send_keys(postalCode)

    def user_information(self, username, password, confirmpassword):
        self.driver.find_element(By.XPATH, self.userName_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.confirmPassword_xpath).send_keys(confirmpassword)
        self.driver.find_element(By.XPATH, self.submitButton_xpath).click()
        self.driver.find_element(By.XPATH, self.registerText_xpath)
