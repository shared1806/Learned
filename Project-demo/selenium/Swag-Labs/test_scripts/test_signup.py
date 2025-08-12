# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from utils.selenium_utils import click_element, send_keys_to_element, get_element_text
# from utils.config import Config
# from selenium.webdriver.common.alert import Alert
# from selenium.common.exceptions import NoAlertPresentException

# import time

# class Test_SignUp(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome() 
#         self.driver.get(f"{Config.BASE_URL}")

#         send_keys_to_element(self.driver, By.ID, 'user-name', Config.USERNAME)
#         send_keys_to_element(self.driver, By.ID, 'password', Config.PASSWORD)
#         click_element(self.driver, By.ID, 'login-button') 

#     def test_title(self):
#         expected_title = "Swag Labs 1"
#         actual_title = get_element_text(self.driver, By.CLASS_NAME, 'app_logo')

#         try:
#             # Kiểm tra điều kiện
#             self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but got '{actual_title}'")
            
#         except Exception as e:
#             # Nếu muốn in ra thêm log trước khi fail
#             print(f"Test Failed: {str(e)}")
#             self.fail(f"Test failed due to exception: {str(e)}")
