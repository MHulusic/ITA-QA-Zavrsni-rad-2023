from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_view import BaseView
 
class LoginView(BaseView):  
    USERNAME_ITEM = (By.NAME, "username")
    PASSWORD_ITEM = (By.NAME, "password")
    LOGIN_BUTTON_ITEM = (By.CLASS_NAME, "loginbutton")
    LOGOUT_BUTTON_ITEM = (By.CSS_SELECTOR, "a[href='logout.php']")
    ERR_MESSAGE = (By.CLASS_NAME, "loginMessage")
    
    def login(self,username,password): 

        self.wait_for(self.USERNAME_ITEM)

        usernameAdmin = self.find(self.USERNAME_ITEM)
        passwordAdmin = self.find(self.PASSWORD_ITEM)

        usernameAdmin.send_keys(username)
        passwordAdmin.send_keys(password)

        self.find(self.LOGIN_BUTTON_ITEM).click()

    def loginSuccessful(self):
        logoutButton = self.wait_for(self.LOGOUT_BUTTON_ITEM)
        assert "odjava" in logoutButton.text.lower(), "Login is not successful"
    
    def loginUnsuccessful(self):
        errorMessage = self.wait_for(self.ERR_MESSAGE)
        assert "neispravno" in errorMessage.text.lower(), "Login is successful or there is no warrning message"



