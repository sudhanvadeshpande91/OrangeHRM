from logging import Logger

import allure
import pytest

from Utilities.Logger import Logger_class
from Utilities.readConfig import ReadConfig
from pageObjects.Login_Page import Login_Page_Class


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001:
    driver=None
    username= ReadConfig.get_username()
    password= ReadConfig.get_password()
    url= ReadConfig.get_url()
    log= Logger_class.get_logger()

    @allure.title("Verify OrangeHRM Login")
    @allure.description("Here we are verifying login page of OrangeHRM.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(rerun=1,reruns_delay=1)
    def test_verify_url_001(self):
        self.log.info("Starting testcase_001 of OrangeHRM")
        self.log.info("Verifying URL of OrangeHRM")
        self.driver.get(self.url)
        if self.driver.title== "OrangeHRM":
            self.log.info("URL verified successfully and taking screenshot")
            self.driver.save_screenshot("screenshots\\test_verify_url_PASS.png")
            allure.attach.file("screenshots\\test_verify_url_pass.png", name="test_verify_url_pass", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.info("URL verified and taking screenshot")
            self.driver.save_screenshot("screenshots\\test_verify_url_FAIL.png")
            allure.attach.file("screenshots\\test_verify_url_fail.png",name="test_verify_url_fail",attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Testcase_001 is completed")

    def test_OrangeHRM_Login_002(self):
        self.log.info("Starting testcase_002 of OrangeHRM")
        self.driver.get(self.url)
        lp= Login_Page_Class(self.driver)
        self.log.info("Entering Username")
        lp.Enter_Username(self.username)
        self.log.info("Entering Password")
        lp.Enter_Password(self.password)
        lp.Click_Login_Button()
        self.log.info("Login successfully completed")
        if lp.verify_login== "Login Succesful":
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_login_002_PASS.png")
            allure.attach.file("screenshots\\test_OrangeHRM_login_002_PASS.png", name= "test_OrangeHRM_Login_002", attachment_type=allure.attachment_type.PNG)
            lp.Click_Menu_Button()
            lp.Click_Logout_Button()
            assert True
        else:
            self.log.info("Login Fail")
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_login_002_FAIL.png")
            allure.attach.file("screenshots\\test_OrangeHRM_login_002_FAIL.png", name= "test_OrangeHRM_Login_002", attachment_type=allure.attachment_type.PNG)
        self.log.info("Testcase_002 is completed")

