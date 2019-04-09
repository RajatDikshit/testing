class screenshot:

    def __init__(self,driver):
        self.driver=driver
        self.path= "/Users/rajesh/PycharmProjects/MakeMyTripTest/ScreenShots/"

    def capturescreenshot(self,filename):
        self.driver.get_screenshot_as_file(self.path+filename)
