from django.test import TestCase
import time

# Create your tests here.
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from selenium import webdriver

class MySeleniumTests(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()
    
    def test_signin(self):
        #print(self.live_server_url)  # print the live server URL to the console
        driver = webdriver.Chrome()
        driver.get('%s%s' % (self.live_server_url, '/signin'))
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
    
    def test_find_bus(self):
        driver = webdriver.Chrome()
        driver.get('%s%s' % (self.live_server_url, '/signin'))
        username_input = driver.find_element(By.NAME, "name")
        username_input.send_keys('admin')
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('password')
        submit_button = driver.find_element(By.XPATH, '//button[@type="Submit"]')
        submit_button.click()
        driver.get('%s%s' % (self.live_server_url, '/findbus'))
        time.sleep(5)
        driver.quit()
        
    def test_see_bookings(self):
        driver = webdriver.Chrome()
        driver.get('%s%s' % (self.live_server_url, '/signin'))
        username_input = driver.find_element(By.NAME, "name")
        username_input.send_keys('admin')
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('password')
        submit_button = driver.find_element(By.XPATH, '//button[@type="Submit"]')
        submit_button.click()
        driver.get('%s%s' % (self.live_server_url, '/seebookings'))
        time.sleep(5)
        driver.quit()
        
    def test_admin(self):
        driver = webdriver.Chrome()
        driver.get('%s%s' % (self.live_server_url, '/admin'))
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys('admin')
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys('password')
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
        submit_button.click()
        driver.quit()