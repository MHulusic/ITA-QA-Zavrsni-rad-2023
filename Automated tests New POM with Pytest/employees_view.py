from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base_view import BaseView

class EmployeesView(BaseView):  
    FIRST_NAME = (By.NAME, "firstname")
    LAST_NAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    PHONE_NR = (By.NAME, "phone")
    OFFICE = (By.ID, "office_id")
    UNIT = (By.ID, "organization_id")
    SAVE_BUTTON_ITEM = (By.NAME, "save")
    SEARCH_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.NAME, "employeesSearch")
    DELETE_EMPLOYEE = (By.CSS_SELECTOR, "button[class='button red']")
    DEL_CONFIRM = (By.ID, "del")
    TABLE = (By.CSS_SELECTOR, "div[class='table emptable']")
    ALL_USERS = (By.TAG_NAME, "tr")
    USER = (By.TAG_NAME, "td")
            
    def newEmployee(self, firstname, lastname, email, phone, officeNo, orgUnit): 

        self.wait_for(self.FIRST_NAME)

        nameNew = self.find(self.FIRST_NAME)
        nameNew.send_keys(firstname)

        lastNameNew = self.find(self.LAST_NAME)
        lastNameNew.send_keys(lastname)
        emailNew = self.find(self.EMAIL)
        emailNew.send_keys(email)
        phoneNew = self.find(self.PHONE_NR)
        phoneNew.send_keys(phone)
        role_dropdown_1 = self.find(self.OFFICE)
        role_select = Select(role_dropdown_1)
        role_select.select_by_visible_text(officeNo)
        role_dropdown_2 = self.find(self.UNIT)
        role_select = Select(role_dropdown_2)
        role_select.select_by_visible_text(orgUnit)

        self.find(self.SAVE_BUTTON_ITEM).click()
         
    def searchEmployee(self, firstname):
                
        self.wait_for(self.SEARCH_FIELD)
        searchEmployee = self.find(self.SEARCH_FIELD)
        searchEmployee.send_keys(firstname)
        searchButton = self.find(self.SEARCH_BUTTON)
        searchButton.click()

    def deleteEmployee(self):
                                
        self.wait_for(self.DELETE_EMPLOYEE)
        deleteEmployee = self.find(self.DELETE_EMPLOYEE)
        deleteEmployee.click()

        self.wait_for(self.DEL_CONFIRM)

        deleteConfirm = self.find(self.DEL_CONFIRM)
        deleteConfirm.click()

    def employeeExistInDB(self, firstname):
        table = self.wait_for(self.TABLE)
        users = table.find_elements(By.TAG_NAME, "tr")
        atributes = []
        for user in users:
            cells = user.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                atributes.append(cell.text)
                                
        assert firstname in atributes, f"Employee {firstname} does not exist in the database"

    '''def employeeDoNotExistInDB(self, firstname):
        table = self.wait_for(self.TABLE)
        users = table.find_elements(By.TAG_NAME, "tr")

        for user in users:
            user_data = user.text
            if firstname.strip().lower() in user_data.strip().lower():
                assert False, f"Employee {firstname} still exists in the database"
        '''
    
    def employeeDoNotExistInDB(self, firstname):
        table = self.wait_for(self.TABLE)
        users = table.find_elements(By.TAG_NAME, "tr")
        
        if not users:
            return

        for user in users:
            cells = user.find_elements(By.TAG_NAME, "td")
            assert not cells, f"Employee {firstname} still exists in the database"

            


