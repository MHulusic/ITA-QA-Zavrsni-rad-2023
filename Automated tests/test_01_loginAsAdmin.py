'''Automated test script that login as Admin on website 'Evidencija Racunarske Opreme'. The same Admin is then logged out. '''
def Test01(): 

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from credentials import adminUsername
    from credentials import adminPassword

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

    title = driver.find_element(By.CSS_SELECTOR, "a[href='index.php']")
    
    test_result_01 = ""
    
    if title.text == "EVIDENCIJA RAČUNARSKE OPREME":
        test_result_01 = "Test no.01 passed! Admin " + myUsername + " is successfully logged in."
    else:
        test_result_01 = "Test no.01 failed! Admin is not logged in."


    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_01

