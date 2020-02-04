class HomePage():
    def __init__(self,driver):
        self.driver = driver;

        self.welcome_link_xpath = "//a[@id='welcome']"
        self.logout_link_xpath = "//a[contains(text(),'Logout')]"

    def click_welcome_link(self):
        self.driver.find_element_by_xpath(self.welcome_link_xpath).click()

    def click_logout_link(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()