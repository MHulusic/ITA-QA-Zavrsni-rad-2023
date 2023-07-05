'''Automated test script login as Admin and creates a new Admin profile on website section 'Administracija Korisnika' on website 'Evidencija Racunarske Opreme'.  '''
def Test03():

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from selenium.webdriver.support.select import Select
    from credentials import adminUsername
    from credentials import adminPassword
    from credentials import newAdminFirstname
    from credentials import newAdminLastname
    from credentials import newAdminUsername
    from credentials import newAdminPassword

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

    firstNameUser = driver.find_element(By.NAME, "firstname")
    lastNameUser = driver.find_element(By.NAME, "lastname")
    userNameUser = driver.find_element(By.NAME, "username")
    passWordUser = driver.find_element(By.NAME, "pass")

    firstname = newAdminFirstname()
    lastname = newAdminLastname()
    username = newAdminUsername()
    password = newAdminPassword()

    firstNameUser.send_keys(firstname)
    lastNameUser.send_keys(lastname)
    userNameUser.send_keys(username)
    passWordUser.send_keys(password)

    role_dropdown = driver.find_element(By.ID, "role")
    role_select = Select(role_dropdown)
    role_select.select_by_visible_text("Administrator")

    saveUser = driver.find_element(By.NAME, "saveUser")
    saveUser.click()

    time.sleep(2)

    allUsers = driver.find_elements(By.TAG_NAME, "tr")

    test_result_03 = ""
    
    for user in allUsers:
        if firstname in user.text and lastname in user.text:
            infoUser = user.find_elements(By.TAG_NAME, "td")
            listOfAtributes = []
            for info in infoUser:
                listOfAtributes.append(info.text)
            test_result_03 = f"Test no.03 passed! Admin profile with firstname = {listOfAtributes[1]}, lastname = {listOfAtributes[2]} is successfully added to table users at {listOfAtributes[0]}. position"
            break
        else:
            test_result_03 = f"Test no.03 failed! Admin profile is not created"

    time.sleep(4)

    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_03