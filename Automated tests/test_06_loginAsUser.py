'''Automated test script that login as User on website 'Evidencija Racunarske Opreme'. The same Admin is then logged out. '''

def Test06():

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from selenium.webdriver.support.select import Select
    from credentials import newUserUsername
    from credentials import newUserPassword

    option = Options()

    option.add_argument("start-maximized")

    driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')

    driver.get("https://puppies-closet.com/evidencija/login.php")

    time.sleep(2)

    userUsername = newUserUsername()
    userPassword = newUserPassword()

    usernameUser = driver.find_element(By.NAME, "username")
    passwordUser = driver.find_element(By.NAME, "password")

    usernameUser.send_keys(userUsername)
    passwordUser.send_keys(userPassword)

    loginUser = driver.find_element(By.CLASS_NAME, "loginbutton")
    loginUser.click()

    time.sleep(2)

    time.sleep(5)

    title = driver.find_element(By.CSS_SELECTOR, "a[href='index.php']")
    
    test_result_06 = ""
    
    if title.text == "EVIDENCIJA RAČUNARSKE OPREME":
        test_result_06 = "Test no.06 passed! User " + userUsername + " is successfully logged in."
    else:
        test_result_06 = "Test no.06 failed! User is not logged in."


    logout = driver.find_element(By.CLASS_NAME, "logout")
    logout.click()

    driver.quit()

    return test_result_06

