from selenium import webdriver
import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from sample.POMModel.Pages.loginPage import LoginPage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

     @classmethod
     def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


     def test_login_valid(self):

        driver = self.driver
        driver.get("https://www.saucedemo.com/v1/")
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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/vidyasehgal/PycharmProjects/Automation/reports"))
