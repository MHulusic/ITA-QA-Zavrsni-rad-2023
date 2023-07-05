'''An automated test script that logs in as an Admin on the website 'Evidencija Računarske Opreme' and searches for an employee by name.'''

def Test09(): 

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

    test_result_09 = ""

    for employee in allEmployees:
        if firstname in employee.text and lastname in employee.text:
            infoEmployee = employee.find_elements(By.TAG_NAME, "td")
            listOfAtributes = []
            for info in infoEmployee:
                listOfAtributes.append(info.text)
            if listOfAtributes[0] == "1":
                test_result_09 = f"Test no.09 passed! New employee with firstname = {listOfAtributes[1]}, lastname = {listOfAtributes[2]} is successfully found with search functionality."
                break
            else:
                test_result_09 = f"Test no.09 failed! New employee is not found with search functionality."

    time.sleep(2)

    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_09