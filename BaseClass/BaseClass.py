from selenium import webdriver
from Utilities.ScreenShot import screenshot
import unittest

class BaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome("/Users/rajesh/Downloads/chromedriver")
        cls.driver.get("https://www.makemytrip.com/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def takescreenshot(self,filename):
        scnobj=screenshot(self.driver)
        scnobj.capturescreenshot(filename)


    @classmethod
    def tearDownClass(cls):
        print("Test successfull")
        cls.driver.close()
        cls.driver.quit()
