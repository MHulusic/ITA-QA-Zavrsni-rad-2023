'''An automated test script that tries to log in as an Admin on the website 'Evidencija Računarske Opreme' with incorrect credentials.'''
def Test02(): 

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time 
    from credentials import incorrectAdminUsername
    from credentials import incorrectAdminPassword

    option = Options()

    option.add_argument("start-maximized")

    driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')

    driver.get("https://puppies-closet.com/evidencija/login.php")

    time.sleep(2)

    myUsername = incorrectAdminUsername()
    myPassword = incorrectAdminPassword()

    usernameAdmin = driver.find_element(By.NAME, "username")
    passwordAdmin = driver.find_element(By.NAME, "password")

    usernameAdmin.send_keys(myUsername)
    passwordAdmin.send_keys(myPassword)

    loginAdmin = driver.find_element(By.CLASS_NAME, "loginbutton")
    loginAdmin.click()

    time.sleep(5)

    message = driver.find_element(By.CLASS_NAME, "loginMessage")
    
    test_result_02 = ""
    
    if message.text == "Neispravno korisničko ime ili lozinka.":
        test_result_02 = "Test no.02 passed! The login with incorrect credentials is unsuccessful, and an alert is displayed for incorrect credentials. "
    else:
        test_result_02 = "Test no.02 failed!"


    driver.quit()

    return test_result_02

