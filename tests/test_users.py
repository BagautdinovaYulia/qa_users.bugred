import pickle
import time
import allure

from pages.users_page import UsersPage


@allure.suite("Пользователи")
@allure.feature("")
class TestUsers:

    # апи для создания пользователя

    @allure.title("Проверка удаления пользователя")
    def test_delete_user(self, driver):
        driver.get("http://users.bugred.ru/user/admin/index.html")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        users_page = UsersPage(driver, "http://users.bugred.ru/user/admin/index.html")
        users_page.open()
        users_page.delete_user()
        time.sleep(1)

    @allure.title("Проверка, что пользователь удален")
    def test_check_new_user(self, driver):


# class TestLogout:

    # def test_logout(self, driver):
