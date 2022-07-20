import time
import requests
from pages.users_page import UsersPage


class TestUsers:

    # апи для создания пользователя
    def test_delete_user(self, driver):
        users_page = UsersPage(driver, requests.post("http://users.bugred.ru/user/admin/index.html",
                                                     data={"login": "7dazzlestar3bagautd@gmail.com",
                                                           "password": "12345qa"}))
        users_page.open()
        users_page.delete_user()
        time.sleep(1)

    # def test_check_new_user(self, driver):

# class TestLogout:

    # def test_logout(self, driver):
