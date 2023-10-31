from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base_view import BaseView

class EquipmentView(BaseView):  
    EQ_VIEW = (By.CSS_SELECTOR, "a[href='index.php?page=equipment']")
    EQ_TYPE = (By.ID, "type_id")
    EQ_PRODUCER = (By.ID, "producer_id")
    INVENTORY_NO = (By.NAME, "inventoryNumber")
    SERIAL_NO = (By.NAME, "serialNumber")
    UNIT = (By.ID, "organization_id")
    SAVE_BUTTON = (By.NAME, "save")
    SEARCH_FIELD = (By.NAME, "equSearch")
    SEARCH_BUTTON = (By.NAME, "equipmentSearch")
    DELETE_EQ = (By.CSS_SELECTOR, "button[class='button red']")
    DEL_CONFIRM = (By.ID, "del")
    TABLE = (By.CSS_SELECTOR, "div[class='table equtable']")
    ALL_EQUIPMENT = (By.TAG_NAME, "tr")
    EQUIPMENT = (By.TAG_NAME, "td")
            
    def goToEquipmentView(self): 
        self.wait_for(self.EQ_VIEW).click()

    def addNewEquipment(self,eqType,eqProducer,inventoryNumber,serialNumber):
        self.wait_for(self.EQ_TYPE)
        
        role_dropdown_1 = self.find(self.EQ_TYPE)
        role_select = Select(role_dropdown_1)
        role_select.select_by_visible_text(eqType)

        role_dropdown_2 = self.find(self.EQ_PRODUCER)
        role_select = Select(role_dropdown_2)
        role_select.select_by_visible_text(eqProducer)

        inventoryNumberEQ = self.find(self.INVENTORY_NO)
        serialNumberEQ = self.find(self.SERIAL_NO)
    
        inventoryNumberEQ.send_keys(inventoryNumber)
        serialNumberEQ.send_keys(serialNumber)
    
        self.find(self.SAVE_BUTTON).click()
             
    def searchEquipment(self, inventoryNumber):
                
        self.wait_for(self.SEARCH_FIELD)
        searchEmployee = self.find(self.SEARCH_FIELD)
        searchEmployee.send_keys(inventoryNumber)
        self.find(self.SEARCH_BUTTON).click()

    def deleteEquipment(self):
                                
        self.wait_for(self.DELETE_EQ)
        deleteEmployee = self.find(self.DELETE_EQ)
        deleteEmployee.click()

        self.wait_for(self.DEL_CONFIRM)

        deleteConfirm = self.find(self.DEL_CONFIRM)
        deleteConfirm.click()

    def equipmentExistInDB(self, inventoryNumber):
        table = self.wait_for(self.TABLE)
        allEquipment = table.find_elements(By.TAG_NAME, "tr")
        atributes = []
        for equipment in allEquipment:
            cells = equipment.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                atributes.append(cell.text)
                                
        assert inventoryNumber in atributes, f"Equipment with inventory no. {inventoryNumber} does not exist in the database"

    def equipmentDoNotExistInDB(self, serialNumber):
        table = self.wait_for(self.TABLE)
        allEquipment = table.find_elements(By.TAG_NAME, "tr")
        
        if not allEquipment:
            return

        for equipment in allEquipment:
            cells = equipment.find_elements(By.TAG_NAME, "td")
            assert not cells, f"Equipment with serial no. {serialNumber} still exists in the database"
