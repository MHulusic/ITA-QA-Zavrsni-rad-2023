'''
Single Test Runner is script that runs single selected test script prepared for website 'Evidencija Racunarske Opreme' and print report on terminal. 

IMPORTANT:

-you have to enter full test name and test function
'''

from test_03_addNewAdmin import Test03
result = Test03()
print("Test results is:", result)

