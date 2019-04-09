from selenium import webdriver
import unittest
from BaseClass.BaseClass import BaseClass
from Pages.LoginPage import Login


class LoginTest(BaseClass):

    def test_01login(self):
        self.Loogin = Login(self.driver)
        self.Loogin.Openloginpage()
        self.takescreenshot(filename="makemytrip1.png")

    def test_02username(self):
        self.Username = Login(self.driver)
        self.Username.enterusername()
        self.takescreenshot(filename="makemytrip2.png")


    def test_03password(self):
        self.Password = Login(self.driver)
        self.Password.enterpassword()
        self.takescreenshot(filename="makemytrip3.png")

    def test_04username(self):
        self.loginclick = Login(self.driver)
        self.loginclick.clickloginbutton()

#if __name__=='__main__':
    #unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output="/Users/rajesh/PycharmProjects/MakeMyTripTest/TestReports/"))


