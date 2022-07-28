import pickle
import time
import allure
import pytest

from pages.login_page import LoginPage, RegistrationPage


@allure.suite("Логин")
@allure.feature("Регистрация")
class TestRegistration:

    @allure.title("Проверка регистрации")
    @pytest.mark.reg
    def test_registration(self, driver):
        registration_page = RegistrationPage(driver, 'http://users.bugred.ru/user/register/')
        users_page = RegistrationPage(driver, "http://users.bugred.ru/admin/")
        with allure.step("Открытие страницы логина"):
            registration_page.open()
        with allure.step("Заполнение полей"):
            registration_page.fill_registration_fields()
            time.sleep(1)
        with allure.step("Проверка успешной регистрации"):
            users_page.check_registration()

        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        driver.quit()


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Проверка авторизации")
    def test_login(self, driver):
        login_page = LoginPage(driver, 'http://users.bugred.ru/user/login/')
        users_page = RegistrationPage(driver, "http://users.bugred.ru/admin/")
        with allure.step("Открытие страницы логина"):
            login_page.open()
        with allure.step("Заполнение полей"):
            login_page.fill_login_fields()
            time.sleep(1)
        with allure.step("Проверка успешной авторизации"):
            users_page.check_registration()
