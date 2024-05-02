from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_signin():
        #print(self.live_server_url)  # print the live server URL to the console
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        username_input = driver.find_element(By.NAME, "name")
        username_input.send_keys('admin')
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('password')
        submit_button = driver.find_element(By.XPATH, '//button[@type="Submit"]')
        submit_button.click()
        #time.sleep(5)
        driver.quit()
        
    # def test_signup(self):
    #     driver = webdriver.Chrome()
    #     driver.get('%s%s' % (self.live_server_url, '/signup'))
    #     username_input = driver.find_element(By.NAME, "email")
    #     username_input.send_keys('test_user1@gmail.com')
    #     password_input = driver.find_element(By.NAME, "name")
    #     password_input.send_keys('test_user1')
    #     confirm_password_input = driver.find_element(By.NAME, "password")
    #     confirm_password_input.send_keys('password')
    #     submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    #     submit_button.click()
    #     driver.quit()

def test_find_bus():
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        username_input = driver.find_element(By.NAME, "name")
        username_input.send_keys('admin')
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('password')
        submit_button = driver.find_element(By.XPATH, '//button[@type="Submit"]')
        submit_button.click()
        driver.get('http://127.0.0.1:8000/findbus')
        driver.quit()
        
def test_see_bookings():
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        username_input = driver.find_element(By.NAME, "name")
        username_input.send_keys('admin')
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('password')
        submit_button = driver.find_element(By.XPATH, '//button[@type="Submit"]')
        submit_button.click()
        driver.get('http://127.0.0.1:8000/seebookings')
        driver.quit()
        
def test_admin():
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/admin')
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys('admin')
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('password')
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
        submit_button.click()
        driver.quit()