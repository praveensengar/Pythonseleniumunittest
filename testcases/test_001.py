
from pages.keyword import TESTREGISTRATION
from testcases.generic import GENERICLASS
import unittest
import HtmlTestRunner
html_report_dir = '..\\report'

class TESTCASES(unittest.TestCase,TESTREGISTRATION):

    def __init__(self,driver):
        super().__init__(driver)
        self.test_generic = GENERICLASS()
        self.test_reg = TESTREGISTRATION()

    def test_Automate_User_Registration_Process(self):
        self.test_generic.setUp()
        self.test_reg.enter_the_First_and_last_name("Praveen", "Singh")
        self.test_reg.select_the_gender()
        self.test_reg.enter_the_address("City: Noida, Flat:A19,PINCODE: 12121212, Mob.: 8787878787")
        self.test_reg.enter_the_street_address("Saviour green A19")
        self.test_reg.enter_the_optional_data("No data require")
        self.test_reg.enter_the_city_name("Noida")
        self.test_reg.select_the_State()
        self.test_reg.enter_the_email("leadersenger@gmail.com")
        self.test_reg.enter_the_date_of_demo("1/2/2022")
        self.test_reg.select_the_course()
        self.test_reg.enter_the_query("No querry")
        self.test_reg.Enter_verification_digit("78")
        self.test_reg.click_on_submit_button()
        self.test_reg.verify_form_is_submitted()
        self.test_generic.tearDown()



if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir))