'''Automated test script that login as Admin on website 'Evidencija Racunarske Opreme' and add new equipment. The same equipment is later deleted'''

def Test12(): 

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
    
    inventoryNumber = newInventoryNumber()
    serialNumber = newSerialNumber()
    
    
    time.sleep(2)

    searchEQ = driver.find_element(By.NAME, "equSearch")
    searchEQ.send_keys(inventoryNumber)
    searchButton = driver.find_element(By.NAME, "equipmentSearch")
    searchButton.click()

    time.sleep(2)

    allEQ = driver.find_elements(By.TAG_NAME, "tr")

    test_result_06 = ""

    for equipment in allEQ:
        if inventoryNumber in equipment.text and serialNumber in equipment.text:
            infoEQ = equipment.find_elements(By.TAG_NAME, "td")
            listOfAtributes = []
            
            for info in infoEQ:
                listOfAtributes.append(info.text)

            time.sleep(2)

            deleteEQ = driver.find_element(By.CSS_SELECTOR, "button[class='button red']")
            deleteEQ.click()

            time.sleep(4)

            deleteConfirm = driver.find_element(By.ID, "del")
            deleteConfirm.click()

            break

    time.sleep(2)

    searchEQ = driver.find_element(By.NAME, "equSearch")
    searchEQ.send_keys(inventoryNumber)
    searchButton = driver.find_element(By.NAME, "equipmentSearch")
    searchButton.click()

    time.sleep(2)

    allEQ = driver.find_elements(By.TAG_NAME, "tr")

    test_result_12 = ""

    for equipment in allEQ:
        if inventoryNumber in equipment.text and serialNumber in equipment.text:
            test_result_12 = f"Test no.12 failed! Equipment is not deleted."
            break
        else:
            test_result_12 = f"Test no.12 passed! Equipment with type = {listOfAtributes[1]}, producer = {listOfAtributes[2]} is deleted from table equipment."

    time.sleep(2)

    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_12