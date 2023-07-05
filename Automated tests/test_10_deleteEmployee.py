'''An automated test script that logs in as an Admin on the website 'Evidencija Računarske Opreme' and deletes an employee.'''

def Test10(): 

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from selenium.webdriver.support.select import Select
    from credentials import adminUsername
    from credentials import adminPassword
    from credentials import newEmployeeFirstname
    from credentials import newEmployeeLastname
    
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

    firstname = newEmployeeFirstname()
    lastname = newEmployeeLastname()
    
    time.sleep(2)

    searchEmployee = driver.find_element(By.NAME, "search")
    searchEmployee.send_keys(firstname)
    searchButton = driver.find_element(By.NAME, "employeesSearch")
    searchButton.click()

    time.sleep(2)

    allEmployees = driver.find_elements(By.TAG_NAME, "tr")

    test_result_10 = ""

    for employee in allEmployees:
        if firstname in employee.text and lastname in employee.text:
            infoEmployee = employee.find_elements(By.TAG_NAME, "td")
            listOfAtributes = []
            for info in infoEmployee:
                listOfAtributes.append(info.text)
            time.sleep(2)

            deleteEmployee = driver.find_element(By.CSS_SELECTOR, "button[class='button red']")
            deleteEmployee.click()

            time.sleep(4)

            deleteConfirm = driver.find_element(By.ID, "del")
            deleteConfirm.click()

    time.sleep(2)

    searchEmployee = driver.find_element(By.NAME, "search")
    searchEmployee.send_keys(firstname)
    searchButton = driver.find_element(By.NAME, "employeesSearch")
    searchButton.click()

    time.sleep(2)

    allEmployees = driver.find_elements(By.TAG_NAME, "tr")

    test_result_10 = ""

    for employee in allEmployees:
        if firstname in employee.text and lastname in employee.text:
            test_result_10 = f"Test no.10 failed! Employee with firstname = {listOfAtributes[1]}, lastname = {listOfAtributes[2]} is not deleted from table employees."
        else:
            test_result_10 = f"Test no.10 passed! Employee with firstname = {listOfAtributes[1]}, lastname = {listOfAtributes[2]} is successfully deleted from table employees."

    time.sleep(4)

    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_10