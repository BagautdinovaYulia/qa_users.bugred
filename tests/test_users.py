import time

from pages.users_page import UsersPage


class TestUsers:

    def test_delete_user(self, driver):
        users_page = UsersPage(driver, 'http://users.bugred.ru/user/admin/index.html')
        users_page.open()
        users_page.delete_user()
        time.sleep(3)

    # def test_check_new_user(self, driver):

# class TestLogout:

    # def test_logout(self, driver):
