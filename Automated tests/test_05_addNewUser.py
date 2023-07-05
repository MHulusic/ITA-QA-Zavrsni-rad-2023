'''Automated test script login as Admin and creates a new User profile on website section 'Administracija Korisnika' on website 'Evidencija Racunarske Opreme'. '''

def Test05():

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from selenium.webdriver.support.select import Select
    from credentials import adminUsername
    from credentials import adminPassword
    from credentials import newUserFirstname
    from credentials import newUserLastname
    from credentials import newUserUsername
    from credentials import newUserPassword

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

    firstname = newUserFirstname()
    lastname = newUserLastname()
    username = newUserUsername()
    password = newUserPassword()

    firstNameUser.send_keys(firstname)
    lastNameUser.send_keys(lastname)
    userNameUser.send_keys(username)
    passWordUser.send_keys(password)

    role_dropdown = driver.find_element(By.ID, "role")
    role_select = Select(role_dropdown)
    role_select.select_by_visible_text("Korisnik")

    saveUser = driver.find_element(By.NAME, "saveUser")
    saveUser.click()

    time.sleep(4)

    test_result_05 = ""

    allUsers = driver.find_elements(By.TAG_NAME, "tr")
    for user in allUsers:
        if firstname in user.text and lastname in user.text:
            infoUser = user.find_elements(By.TAG_NAME, "td")
            listOfAtributes = []
            for info in infoUser:
                listOfAtributes.append(info.text)
            test_result_05 = f"Test no. 05 passed! User profile with firstname = {listOfAtributes[1]}, lastname = {listOfAtributes[2]} is successfully added to table users."
            break
        else:
            test_result_05 = f"Test no.05 failed! User profile is not created"


    time.sleep(4)

    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()
    
    return test_result_05