from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
import pytest

class Test_Demo2Class:
    
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")))
        addToCart.click()
        self.driver.execute_script("window.scrollTo(0,500)") 
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
        addToCart.click()
        self.driver.execute_script("window.scrollTo(500,0)") 
        shoppingCartLink = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        shoppingCartLink.click()

    def teardown_method(self): 
        self.driver.quit()
    
    def test_add_to_cart(self):
        
        listOfCourses = self.driver.find_elements(By.CLASS_NAME,"cart_item")
        assert len(listOfCourses) == 2

    def test_remove_from_cart(self):
        remove = WebDriverWait(self.driver,8).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-sauce-labs-backpack']")))
        remove.click()
        remove = WebDriverWait(self.driver,8).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-test.allthethings()-t-shirt-(red)']")))
        remove.click()
        listOfCourses = self.driver.find_elements(By.CLASS_NAME,"cart_item")
        assert len(listOfCourses) == 0

    @pytest.mark.parametrize("firstName,lastName,postalCode",[("eda","sarı","")])
    
    def test_checkout(self,firstName,lastName,postalCode):
        checkout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkout.click()
        firstNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        firstNameInput.send_keys(firstName)
       
        lastNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"last-name")))
        lastNameInput.send_keys(lastName)

        postalCodeInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        postalCodeInput.send_keys(postalCode)

        continueButton = self.driver.find_element(By.ID,"continue")
        continueButton.click()
       
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")
        assert errorMessage.text == "Error: Postal Code is required"
    