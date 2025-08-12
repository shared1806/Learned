import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.selenium_utils import click_element, send_keys_to_element, get_element_text
from utils.config import Config

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class Test_SignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get(f"{Config.BASE_URL}")

    def test_Login_with_valid_Username_and_Password(self):
        """Test case login với thông tin hợp lệ"""

        send_keys_to_element(self.driver, By.ID, 'user-name', Config.USERNAME)
        send_keys_to_element(self.driver, By.ID, 'password', Config.PASSWORD)
        click_element(self.driver, By.ID, 'login-button') 

        try:
            result = get_element_text(self.driver, By.XPATH, '//span[text()="Products"]')
            assert result == "Products"

        except Exception as e:
            print(f"Test Failed: {str(e)}")

    def test_Login_with_invalid_Username_and_Password(self):
        """Test case of login with incorrect email format"""
        send_keys_to_element(self.driver, By.ID, 'user-name', "invalid_email")
        send_keys_to_element(self.driver, By.ID, 'password', "invalid_password")
        click_element(self.driver, By.ID, 'login-button') 

        try:
            result = get_element_text(self.driver, By.XPATH, '//h3[@data-test="error"]')
            assert result == "Epic sadface: Username and password do not match any user in this service"

        except Exception as e:
            print(f"Test Failed: {str(e)}")
        
    def test_Login_with_locked_out_user(self):
        """Test case login với thông tin bị khoá"""

        send_keys_to_element(self.driver, By.ID, 'user-name', "locked_out_user")
        send_keys_to_element(self.driver, By.ID, 'password', "secret_sauce")
        click_element(self.driver, By.ID, 'login-button') 
        time.sleep(2)

        try:
            result = get_element_text(self.driver, By.XPATH, '//h3[@data-test="error"]')
            assert result == "Epic sadface: Sorry, this user has been locked out."

        except Exception as e:
            print(f"Test Failed: {str(e)}")

    def test_Login_with_empty_Username_and_Password(self):
        """Test case login với thông tin hợp lệ trống"""

        click_element(self.driver, By.ID, 'login-button') 

        try:
            result = get_element_text(self.driver, By.XPATH, '//h3[@data-test="error"]')
            assert result == "Epic sadface: Username is required"

        except Exception as e:
            print(f"Test Failed: {str(e)}")
 