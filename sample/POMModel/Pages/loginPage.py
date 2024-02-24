from selenium.webdriver.common.by import By
from sample.POMModel.Locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_id = Locators.login_button_id


    def enter_username(self, username):

        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys("standard_user")


    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys("secret_sauce")


    def click_login(self):

        self.driver.find_element(By.ID, self.login_button_id).click()



