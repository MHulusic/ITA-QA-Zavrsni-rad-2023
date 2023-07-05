'''Automated test script login as Admin and deletes created Admin profile on website section 'Administracija Korisnika' on website 'Evidencija Racunarske Opreme'.'''
def Test04():

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from selenium.webdriver.support.select import Select
    from credentials import adminUsername
    from credentials import adminPassword
    from credentials import newAdminFirstname
    from credentials import newAdminLastname
    #from credentials import newAdminUsername
    #from credentials import newAdminPassword

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

    time.sleep(2)

    mainNavigation = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=users']")
    mainNavigation.click()   

    firstname = newAdminFirstname()
    lastname = newAdminLastname()
    #username = newAdminUsername()
    #password = newAdminPassword()

    time.sleep(2)

    allUsers = driver.find_elements(By.TAG_NAME, "tr")

    test_result_04 = ""
    
    for user in allUsers:
        if firstname in user.text and lastname in user.text:
            deleteUser = user.find_element(By.CSS_SELECTOR, "button[class='button red']")
            deleteUser.click()

            time.sleep(4)

            deleteConfirm = driver.find_element(By.ID, "del")
            deleteConfirm.click()
            break
        
    time.sleep(2)

    allUsers = driver.find_elements(By.TAG_NAME, "tr")

    flag = True

    for user in allUsers:
        if firstname in user.text and lastname in user.text:
            test_result_04 = f"Test no.04 failed! Admin profile with firstname = {firstname}, lastname = {lastname} is not successfully deleted from table users."
            flag = False
            break
    
    if flag == True:
        test_result_04 = f"Test no.04 passed! Admin profile with firstname = {firstname}, lastname = {lastname} is successfully deleted from table users."
        
    time.sleep(4)

    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_04