'''
Test Runner is a script that runs all test scripts prepared for the website 'Evidencija Računarske Opreme' and prints a report in a .csv file.

IMPORTANT:

Before running the script, please check if:

- All credentials in "credentials.py" are filled correctly and are unique.
- For test_08_addNewEmployee, please check if the Broj kancelarije "001" and Organizaciona jedinica "TEST OJ" already exist. 
    If not, they MUST BE created before starting this test.
- For test_11_addNewEquipment, please check if the Tip opreme "Test Equipment" and Proizvođač opreme "Test Company" already exist. 
    If not, they MUST BE created before starting this test.
'''


import csv
from datetime import datetime
from test_01_loginAsAdmin import Test01
from test_02_loginAsAdminWithIncorrectCredentials import Test02
from test_03_addNewAdmin import Test03
from test_04_deleteAdmin import Test04
from test_05_addNewUser import Test05
from test_06_loginAsUser import Test06
from test_07_deleteUser import Test07
from test_08_addNewEmployee import Test08
from test_09_searchEmployee import Test09
from test_10_deleteEmployee import Test10
from test_11_addNewEquipment import Test11
from test_12_deleteEquipment import Test12

# Import more test and TestXX functions here

current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"Tests_report_{current_datetime}.csv"

test_functions = [Test01,Test02,Test03,Test04,Test05,Test06,Test07,Test08,Test09,Test10,Test11,Test12]  # Add more test functions here

test_results = []
for test_function in test_functions:
    result = test_function()
    test_results.append(result)

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["TEST RESULTS"])
    for result in test_results:
        writer.writerow([result])

print("Test results written to:", filename)

