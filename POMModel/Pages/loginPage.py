class LoginPage():
    def __int__(self,driver):
        self.driver =driver

        self.username_textbox_name ="user-name"
        self.password_textbox_name ="password"
        self.login_button_id = "login-button"


    def enter_username(self, username):
        self.driver.find_element(self.username_textbox_name).send_keys("standard_user")


    def enter_password(self, password):
        self.driver.find_element(self.password_textbox_name).send_keys("secret_sauce")


    def click_login(self):
        self.driver.find_element(self.login_button_id).click()



