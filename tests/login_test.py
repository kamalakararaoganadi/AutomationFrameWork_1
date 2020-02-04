import time

import egg as egg
from selenium import webdriver
import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from utills import utils as utils
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class Test_login():
    def test_login(self):
        # def test_login(self, test_setup):
        driver = self.driver
        driver.get(utils.URL)
        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()
        loginpage = LoginPage(driver)
        loginpage.enter_user_name(utils.USERNAME)
        loginpage.enter_password(utils.PASSWORD)
        loginpage.click_login_button()

    def test_logout(self):
        try:
            driver = self.driver
            # def test_logout(self, test_setup):
            time.sleep(5)
            # driver.find_element_by_xpath("//a[@id='welcome']").click()
            homepage = HomePage(driver)
            homepage.click_welcome_link()
            time.sleep(1)
            # driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
            homepage.click_logout_link()
            x = driver.title
            assert x=="OrangeHRM1"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currenttime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testname = utils._get_function_name()
            screenshotname = testname+"_"+ currenttime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotname, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/kamalakararao.ganadi/PycharmProjects/AutomationFrameWork_1/screenshots/"+screenshotname+".png")
            raise
        except:
            print("Some exception occurred")
            currenttime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testname = utils._get_function_name()
            screenshotname = testname + "_" + currenttime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotname,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/kamalakararao.ganadi/PycharmProjects/AutomationFrameWork_1/screenshots/" + screenshotname + ".png")

        else:
            print("No exceptions occurred")
        finally:
            print("This block will always execute | Close DB")






