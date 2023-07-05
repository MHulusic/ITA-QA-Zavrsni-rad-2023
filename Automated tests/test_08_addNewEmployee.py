'''An automated test script that logs in as an Admin on the website 'Evidencija Računarske Opreme' and adds a new employee.'''

def Test08(): 

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from selenium.webdriver.support.select import Select
    from credentials import adminUsername
    from credentials import adminPassword
    from credentials import newEmployeeFirstname
    from credentials import newEmployeeLastname
    from credentials import newEmployeeEmail
    from credentials import newEmployeePhone

    option = Options()

    option.add_argument("start-maximized")

    driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')

    driver.get("https://puppies-closet.com/evidencija/login.php")

    time.sleep(2)
 
    myUsername = adminUsername()
    myPassword = adminPassword()

    usernameAdmin = driver.find_element(By.NAME, "username")
    passwordAdmin = driver.find_element(By.NAME, "password")

    usernameAdmin.send_keys(myUsername)
    passwordAdmin.send_keys(myPassword)

    loginAdmin = driver.find_element(By.CLASS_NAME, "loginbutton")
    loginAdmin.click()

    time.sleep(5)

    mainNavigation = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=employees']")
    mainNavigation.click()

    firstNameEmployee = driver.find_element(By.NAME, "firstname")
    lastNameEmployee = driver.find_element(By.NAME, "lastname")
    emailEmployee = driver.find_element(By.NAME, "email")
    phoneEmployee = driver.find_element(By.NAME, "phone")

    firstname = newEmployeeFirstname()
    lastname = newEmployeeLastname()
    email = newEmployeeEmail()
    phone = newEmployeePhone()

    firstNameEmployee.send_keys(firstname)
    lastNameEmployee.send_keys(lastname)
    emailEmployee.send_keys(email)
    phoneEmployee.send_keys(phone)

    role_dropdown_1 = driver.find_element(By.ID, "office_id")
    role_select = Select(role_dropdown_1)
    role_select.select_by_visible_text("001")

    role_dropdown_2 = driver.find_element(By.ID, "organization_id")
    role_select = Select(role_dropdown_2)
    role_select.select_by_visible_text("Test OJ")

    confirmButton = driver.find_element(By.NAME, "save")
    confirmButton.click()

    time.sleep(2)

    searchEmployee = driver.find_element(By.NAME, "search")
    searchEmployee.send_keys(firstname)
    searchButton = driver.find_element(By.NAME, "employeesSearch")
    searchButton.click()

    time.sleep(2)

    allEmployees = driver.find_elements(By.TAG_NAME, "tr")

    test_result_08 = ""

    for employee in allEmployees:
        if firstname in employee.text and lastname in employee.text:
            infoEmployee = employee.find_elements(By.TAG_NAME, "td")
            listOfAtributes = []
            for info in infoEmployee:
                listOfAtributes.append(info.text)
            test_result_08 = f"Test no.08 passed! New employee with firstname = {listOfAtributes[1]}, lastname = {listOfAtributes[2]} is successfully added to table users."
            break
        else:
            test_result_08 = f"Test no.08 failed! New employee is not added."

    time.sleep(4)

    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_08