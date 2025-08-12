from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string

def wait_for_element(driver, by, value, timeout=10):
    """Wait for an element to be present on the page."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def click_element(driver, by, value):
    """Click on a web element."""
    element = wait_for_element(driver, by, value)
    element.click()

def send_keys_to_element(driver, by, value, text):
    """Send keys to a web element."""
    element = wait_for_element(driver, by, value)
    element.clear()
    element.send_keys(text)

def get_element_text(driver, by, value):
    """Get text from a web element."""
    element = wait_for_element(driver, by, value)
    return element.text
