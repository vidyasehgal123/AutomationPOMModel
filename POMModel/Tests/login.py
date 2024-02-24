from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class LoginTest(unittest.TestCase):

     @classmethod
     def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


     def test_login_valid(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

     @classmethod
     def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")



if __name__ == '__main__':
    unittest.main()
