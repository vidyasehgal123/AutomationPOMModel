from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from POMModel.Pages.loginPage import LoginPage

class LoginTest(unittest.TestCase):

     @classmethod
     def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


     def test_login_valid(self):
        driver =self.driver
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()
       # driver.get("https://www.saucedemo.com/v1/")
        #driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        #driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        #driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

     @classmethod
     def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")



if __name__ == '__main__':
    unittest.main()
