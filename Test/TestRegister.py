from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Register import RegisterUser
from selenium.webdriver.support import expected_conditions as EC
from Config.Config import ReadJson as RJ
from drivers.webdriver import WebDriverFactory
from Testdata import testdata as td


class NewTour(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.wdf = WebDriverFactory()
        cls.driver = cls.wdf.getWebDriverInstance()
        # cls.driver = webdriver.Chrome(executable_path="C:/Users/Rohit/PycharmProjects/SeleniumFramework/drivers"
        #                                               "/chromedriver_win32/chromedriver.exe")
        # cls.driver.implicitly_wait(20)
        # cls.driver.maximize_window()

    def test1_register_new_user(self):
        driver = self.driver
        #driver.get("http://newtours.demoaut.com/")
        register = RegisterUser(driver)
        register.contact_information("Rohit", "Tyagi", 6534865849, "a@mailinator.com")
        register.mailing_information("abc", "NewYork", "DC", "DC0003")
        register.user_information(username=td.testData("username"), password=td.testData("password"), confirmpassword=td.testData("passconfirm"))
        # time.sleep(4)
        # exwait = WebDriverWait(driver, 20)
        registration_success = driver.find_element(By.XPATH, "//*[contains(text(), 'Your user name is')]").text
        print(registration_success)
        # exwait.until(EC.presence_of_all_elements_located(registration_success))
        self.assertEqual("Note: Your user name is rtyagi.", registration_success, "Registration Failed!")

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
