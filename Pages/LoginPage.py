from selenium import webdriver
from Locators.Locators import LocatorsPath

class Login:
    def __init__(self,driver):
        self.driver=driver
        self.loginpage= LocatorsPath.loginbutton
        self.username= LocatorsPath.usernameid
        self.password= LocatorsPath.passwordid
        self.clicklogin= LocatorsPath.loginclick

    def Openloginpage(self):
        self.driver.find_element_by_xpath(self.loginpage).click()

    def enterusername(self):
        self.driver.find_element_by_id(self.username).send_keys("rajatd55@gmail.com")

    def enterpassword(self):
        self.driver.find_element_by_id(self.password).send_keys("1*3verifone")

    def clickloginbutton(self):
        self.driver.find_element_by_xpath(self.clicklogin).click()
