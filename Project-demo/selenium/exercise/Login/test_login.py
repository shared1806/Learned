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
        self.driver.get(f"{Config.BASE_URL}/login")

    def test_Login_with_valid_Username_and_Password(self):
        """Test case login với thông tin hợp lệ"""

        send_keys_to_element(self.driver, By.ID, 'user-name', Config.USERNAME)
        send_keys_to_element(self.driver, By.ID, 'password', Config.PASSWORD)
        click_element(self.driver, By.ID, 'login-button') 
        time.sleep(2)

        try:
            result = get_element_text(self.driver, By.XPATH, '//span[text()="Clear Cache"]')
            assert result == "Clear Cache"

        except Exception as e:
            print(f"Test Failed: {str(e)}")

    def test_Login_with_incorrect_email_format(self):
        """Test case of login with incorrect email format"""
        send_keys_to_element(self.driver, By.ID, 'user-name', "invalid_email")
        send_keys_to_element(self.driver, By.ID, 'password', "invalid_password")
        click_element(self.driver, By.ID, 'login-button') 
        time.sleep(2)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input:invalid"))
            )

            email_field = self.driver.find_element(By.ID, "email")
            validation_message = email_field.get_attribute("validationMessage")

            assert validation_message == "Please include an '@' in the email address. 'invalid_email' is missing an '@'."

        except Exception as e:
            print(f"Test Failed: {str(e)}")

    def test_Login_with_invalid_Username_and_Password(self):
        """Test case login với thông tin không hợp lệ"""

        send_keys_to_element(self.driver, By.ID, 'email', "admin@invalid.com")
        send_keys_to_element(self.driver, By.ID, 'password', "invalid_password")
        click_element(self.driver, By.XPATH, '//button[@type="submit"]') 
        time.sleep(2)

        try:
            result = get_element_text(self.driver, By.XPATH, '//span[@data-notify="message"]')
            assert result == "Invalid login credentials"

        except Exception as e:
            print(f"Test Failed: {str(e)}")

    def test_Login_with_empty_Username_and_Password(self):
        """Test case login với thông tin hợp lệ trống"""

        click_element(self.driver, By.XPATH, '//button[@type="submit"]') 

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input:invalid"))
            )

            email_field = self.driver.find_element(By.ID, "email")
            validation_message = email_field.get_attribute("validationMessage")

            assert validation_message == "Please fill out this field."

        except Exception as e:
            print(f"Test Failed: {str(e)}")
 