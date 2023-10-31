# Page Object Model - Smoke tests suite for "Evidencija racunarske opreme" - web app

from login_view import LoginView
from employees_view import EmployeesView
from equipment_view import EquipmentView 
from users_view import UsersView
import time

#1 LOGIN PAGE VIEW
# Master username and password
usernameAdmin, passwordAdmin = 'mustafahulusic','mustafahulusic123' # Do NOT change
# Incorect credentials
incorrectAdminUsername, incorrectAdminPassword = "Hamo", "Hamo123"

def test_01_loginAdmin(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    loginView.loginSuccessful()
    time.sleep(3)

def test_02_loginWithIncorectCredentials(driver):
    loginView = LoginView(driver)
    loginView.login(incorrectAdminUsername, incorrectAdminPassword)
    loginView.loginUnsuccessful()
    time.sleep(3)

#2 EMPLOYEES - COMMISSIONING/DECOMMISSINING OF EQUIPMENT PAGE VIEW
# New employee 
eFirstname,eLastname,eEmail,ePhone = 'TestEmployeeM','TestEmployeeM','testEmployeeM@test.com','123678'
officeNo,orgUnit = "001","Test OJ" # Do NOT change

def test_03_addEmployee(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    employeeView = EmployeesView(driver)
    employeeView.newEmployee(eFirstname, eLastname, eEmail, ePhone, officeNo, orgUnit)
    employeeView.searchEmployee(eFirstname)
    employeeView.employeeExistInDB(eFirstname)
    time.sleep(3)

def test_04_searchEmployee(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    employeeView = EmployeesView(driver)
    employeeView.searchEmployee(eFirstname)
    employeeView.employeeExistInDB(eFirstname)
    time.sleep(3)

def test_05_deleteEmployee(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    employeeView = EmployeesView(driver)
    employeeView.searchEmployee(eFirstname)
    employeeView.deleteEmployee()
    time.sleep(5)
    employeeView.searchEmployee(eFirstname)
    employeeView.employeeDoNotExistInDB(eFirstname)
    time.sleep(3)

#3 EQUIPMENT PAGE VIEW
# New equipment
eqType,eqProducer = "Test Equipment","Test Company" # Do NOT change
inventoryNumber,serialNumber = "TEQ000001","T000001" 

def test_06_regNewEquipment(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    equipmentView = EquipmentView(driver)
    equipmentView.goToEquipmentView()
    equipmentView.addNewEquipment(eqType,eqProducer,inventoryNumber,serialNumber)
    equipmentView.searchEquipment(inventoryNumber)
    equipmentView.equipmentExistInDB(inventoryNumber)
    time.sleep(3)

def test_07_deleteEquipment(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    equipmentView = EquipmentView(driver)
    equipmentView.goToEquipmentView()
    equipmentView.searchEquipment(inventoryNumber)
    equipmentView.deleteEquipment()
    time.sleep(5)
    equipmentView.searchEquipment(serialNumber)
    equipmentView.equipmentDoNotExistInDB(serialNumber)
    time.sleep(3)

#4 USER ADMINISTRATION PAGE VIEW
# New administrator and new user
newAdminFirstname,newAdminLastname,newAdminUsername,newAdminPassword="TestAdminM","TestAdminM","TestAdminM","Test123M"
roleAdmin = 'Administrator' # Do NOT change
newUserFirstname,newUserLastname,newUserUsername,newUserPassword="TestUserM","TestUserM","TestUserM","Test123M"
roleUser = 'Korisnik' # Do NOT change

def test_08_addNewAdmin(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    usersView = UsersView(driver)
    usersView.goToUsersView()
    usersView.addNewUser(newAdminFirstname,newAdminLastname,newAdminUsername,newAdminPassword,roleAdmin)
    usersView.userExistInDB(newAdminFirstname,newAdminLastname,roleAdmin)
    time.sleep(3)

def test_09_deleteAdmin(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    usersView = UsersView(driver)
    usersView.goToUsersView()
    usersView.deleteUser(newAdminFirstname,newAdminLastname)
    time.sleep(3)
    usersView.userDoesNotExistInDB(newAdminFirstname,newAdminLastname)
    time.sleep(3)

def test_10_addNewUser(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    usersView = UsersView(driver)
    usersView.goToUsersView()
    usersView.addNewUser(newUserFirstname,newUserLastname,newUserUsername,newUserPassword,roleUser)
    usersView.userExistInDB(newUserFirstname,newUserLastname,roleUser)
    time.sleep(3)

def test_11_loginAsUser(driver):
    loginView = LoginView(driver)
    loginView.login(newUserUsername, newUserPassword)
    loginView.loginSuccessful()
    time.sleep(3)

def test_12_deleteUser(driver):
    loginView = LoginView(driver)
    loginView.login(usernameAdmin, passwordAdmin)
    usersView = UsersView(driver)
    usersView.goToUsersView()
    usersView.deleteUser(newUserFirstname,newUserLastname)
    time.sleep(3)
    usersView.userDoesNotExistInDB(newUserFirstname,newUserLastname)
    time.sleep(3)
