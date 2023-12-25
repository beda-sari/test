from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
import pytest

class Test_DemoClass:
    
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 

    def teardown_method(self): 
        self.driver.quit()
   
    
    @pytest.mark.parametrize("username,password,error",[("","","Epic sadface: Username is required"),("standard_user","","Epic sadface: Password is required"),("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out.")])
    def test_invalid_login(self,username,password,error):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
       
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
       
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
       
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == error
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_valid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        listOfCourses = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(listOfCourses) == 6
       
        