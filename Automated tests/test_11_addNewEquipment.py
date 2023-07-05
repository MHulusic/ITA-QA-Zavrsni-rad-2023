'''Automated test script that login as Admin on website 'Evidencija Racunarske Opreme' and add new equipment.'''

def Test11(): 

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from selenium.webdriver.support.select import Select
    from credentials import adminUsername
    from credentials import adminPassword
    from credentials import newInventoryNumber
    from credentials import newSerialNumber

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

    mainNavigation = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=equipment']")
    mainNavigation.click()

    time.sleep(2)

    role_dropdown_1 = driver.find_element(By.ID, "type_id")
    role_select = Select(role_dropdown_1)
    role_select.select_by_visible_text("Test Equipment")

    role_dropdown_2 = driver.find_element(By.ID, "producer_id")
    role_select = Select(role_dropdown_2)
    role_select.select_by_visible_text("Test Company")

    inventoryNumberEQ = driver.find_element(By.NAME, "inventoryNumber")
    serialNumberEQ = driver.find_element(By.NAME, "serialNumber")
    
    inventoryNumber = newInventoryNumber()
    serialNumber = newSerialNumber()
    
    inventoryNumberEQ.send_keys(inventoryNumber)
    serialNumberEQ.send_keys(serialNumber)
    
    confirmButton = driver.find_element(By.NAME, "save")
    confirmButton.click()

    time.sleep(2)

    searchEQ = driver.find_element(By.NAME, "equSearch")
    searchEQ.send_keys(inventoryNumber)
    searchButton = driver.find_element(By.NAME, "equipmentSearch")
    searchButton.click()

    time.sleep(2)

    allEQ = driver.find_elements(By.TAG_NAME, "tr")

    test_result_11 = ""

    for equipment in allEQ:
        if inventoryNumber in equipment.text and serialNumber in equipment.text:
            infoEQ = equipment.find_elements(By.TAG_NAME, "td")
            listOfAtributes = []
            for info in infoEQ:
                listOfAtributes.append(info.text)
            test_result_11 = f"Test no.11 passed! New equipment with type = {listOfAtributes[1]}, producer = {listOfAtributes[2]} is successfully added to table users with inentory no. {listOfAtributes[3]} and serial no. {listOfAtributes[4]}."
            break
        else:
            test_result_11 = "Test no.11 failed! New equipment is not added."

    time.sleep(2)

    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_11