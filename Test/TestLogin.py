import driver as driver
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Register import RegisterUser
from selenium.webdriver.support import expected_conditions as EC
from Pages.SignOn import SignOn
from drivers.webdriver import WebDriverFactory
from Testdata import testdata as td


class LoginUser(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.wdf = WebDriverFactory()
        cls.driver = cls.wdf.getWebDriverInstance()
        # cls.driver = webdriver.Chrome(
        #     executable_path="C:/Users/Rohit/PycharmProjects/SeleniumFramework/drivers/chromedriver_win32/chromedriver.exe")
        # cls.driver.implicitly_wait(20)
        # cls.driver.maximize_window()

    def test_login_user(self):
        driver = self.driver
        #driver.get("http://newtours.demoaut.com/")
        login = SignOn(driver)
        login.click_home()
        login.login_user(username=td.testData("username"), password=td.testData("password"))
        login.click_submit()
        flight_details = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr["
                                                      "4]/td/table/tbody/tr/td[2]/table/tbody/tr["
                                                      "5]/td/form/table/tbody/tr[1]/td/font/font/b/font/font").text 
        self.assertEqual("Flight Details", flight_details, "Login Un-Successful")
        
    @classmethod
    def tearDownClass(cls) -> None:
        print("Closing the Browser")
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
