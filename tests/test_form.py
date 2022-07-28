import pickle
import time
import allure

from pages.form_page import FormPage

@allure.suite("Добавить пользователя")
@allure.feature("Добавление пользователя")
class TestForm:

    @allure.title("Проверка создания пользователя")
    def test_form(self, driver):
        driver.get("http://users.bugred.ru/login/")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        form_page = FormPage(driver, "http://users.bugred.ru/admin/index/create")
        users_page = FormPage(driver, "http://users.bugred.ru/admin/")
        with allure.step("Открытие страницы создания пользователя"):
            form_page.open()
        with allure.step("Заполнение и отправка формы"):
            form_page.fill_form_fields()
            time.sleep(1)
        with allure.step("Проверка, что пользователь создан"):
            users_page.check_added_user()
