import time

import allure
import requests

from pages.form_page import FormPage

@allure.suite("Добавить пользователя")
@allure.feature("Добавление пользователя")
class TestForm:

    @allure.title("Проверка создания пользователя")
    def test_form(self, driver):
        form_page = FormPage(driver, "http://users.bugred.ru/user/login")
        form_page.fill_form_fields()
        time.sleep(3)
