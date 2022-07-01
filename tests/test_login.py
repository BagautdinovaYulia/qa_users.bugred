import time

from pages.login_page import LoginPage, RegistrationPage


class TestElements:

    class TestRegistration:

        def test_registration(self, driver):
            registration_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/')
            registration_page.open()
            registration_page.fill_registration_fields.random()
            time.sleep(3)

    class TestLogin:

        def test_login(self, driver):
            login_page = LoginPage(driver, 'http://users.bugred.ru/')
            login_page.open()
            login_page.fill_login_fields()
            time.sleep(3)
