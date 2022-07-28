import pickle
import time
import allure
import requests
from pages.users_page import UsersPage


@allure.suite("Пользователи")
@allure.feature("")
class TestUsers:

    @allure.title("Проверка удаления пользователя")
    def test_delete_user(self, driver):
        with allure.step("Добавили пользователя"):
            information = {
                "id": 1000,
                "username": "testusername",
                "firstName": "testfirstName",
                "lastName": "testlastName",
                "email": "test@testemail.com",
                "password": "12345qa",
                "phone": "+79999999999",
                "userStatus": 1
            }
            requests.post("http://users.bugred.ru/admin/index/create", params=information)

        driver.get("http://users.bugred.ru/user/login/")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        users_page = UsersPage(driver, "http://users.bugred.ru/")
        with allure.step("Открытие страницы пользователей"):
            users_page.open()
        with allure.step("Проверка удаления пользователя"):
            users_page.delete_user()
            time.sleep(1)
        with allure.step("Проверка, что пользователь удален"):
            users_page.check_deleted_user()
