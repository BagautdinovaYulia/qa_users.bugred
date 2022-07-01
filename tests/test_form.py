import time
from test_login import TestElements
from pages.form_page import FormPage

class TestForm:

    def test_open_test_form(self, driver):
        TestElements.TestLogin.test_login(self, driver)

    def test_form(self, driver):
        form_page = FormPage(driver, "http://users.bugred.ru/user/admin/index/create.html")
        form_page.fill_form_fields()
        time.sleep(3)


