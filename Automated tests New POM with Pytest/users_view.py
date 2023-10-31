from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base_view import BaseView

class UsersView(BaseView):  
    USERS_VIEW = (By.CSS_SELECTOR, "a[href='index.php?page=users']")
    NEW_USER_FIRSTNAME = (By.NAME, "firstname")
    NEW_USER_LASTNAME = (By.NAME, "lastname")
    NEW_USER_USERNAME = (By.NAME, "username")
    NEW_USER_PASSWORD = (By.NAME, "pass")
    ROLE = (By.ID, "role")
    SAVE_USER = (By.NAME, "saveUser")
    DELETE_USER = (By.CSS_SELECTOR, "button[class='button red']")
    DEL_CONFIRM = (By.ID, "del")
    ALL_TR_EL = (By.TAG_NAME, "tr")
    TABLE = (By.CSS_SELECTOR, "div[class='table users']")
            
    def goToUsersView(self): 
        self.wait_for(self.USERS_VIEW).click()

    def addNewUser(self,newFirstname,newLastname,newUsername,newPassword,role):
        self.wait_for(self.NEW_USER_FIRSTNAME)

        self.find(self.NEW_USER_FIRSTNAME).send_keys(newFirstname)
        self.find(self.NEW_USER_LASTNAME).send_keys(newLastname)
        self.find(self.NEW_USER_USERNAME).send_keys(newUsername)
        self.find(self.NEW_USER_PASSWORD).send_keys(newPassword)
        
        role_dropdown = self.find(self.ROLE)
        role_select = Select(role_dropdown)
        role_select.select_by_visible_text(role)

        self.find(self.SAVE_USER).click()
             
    def deleteUser(self, newFirstname, newLastname):
        table = self.wait_for(self.TABLE)
        users = table.find_elements(By.TAG_NAME, "tr")

        for user in users:
            if newFirstname in user.text and newLastname in user.text:
                delete_button = user.find_element(By.CSS_SELECTOR, "button[class='button red']")
                delete_button.click()
                self.wait_for(self.DEL_CONFIRM).click()
                break

    def userExistInDB(self, newFirstname,newLastname,role):
        table = self.wait_for(self.TABLE)
        allEquipment = table.find_elements(By.TAG_NAME, "tr")
        
        for equipment in allEquipment:
            cells = equipment.find_elements(By.TAG_NAME, "td")
            atributes = []
            for cell in cells:
                atributes.append(cell.text)
            if newFirstname in atributes and newLastname in atributes and role in atributes:
                break               
        assert newFirstname in atributes, f"User with firstname {newFirstname} does not exist in the database"
                                    
    def userDoesNotExistInDB(self, newFirstname,newLastname):
        table = self.wait_for(self.TABLE)
        allEquipment = table.find_elements(By.TAG_NAME, "tr")
        atributes = []
        for equipment in allEquipment:
            cells = equipment.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                atributes.append(cell.text)
                         
        assert newFirstname not in atributes and newLastname not in atributes, f"User with firstname {newFirstname} still exist in the database"      