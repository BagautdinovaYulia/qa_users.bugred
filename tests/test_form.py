import time
import requests

from pages.form_page import FormPage


class TestForm:

    def test_form(self, driver):
        form_page = FormPage(driver, requests.post("http://users.bugred.ru/user/login", params={"login": "7dazzlestar3bagautd@gmail.com", "password": "12345qa"}))

        form_page.fill_form_fields()
        time.sleep(3)
