import time

from pages.login_page import LoginPage

class TestElements:
    class TestLogin:

        def test(self, driver):
            login_page = LoginPage(driver, 'http://users.bugred.ru/user/login/index.html')
            login_page.open()
            login_page.fill_all_fields()
            time.sleep(3)
