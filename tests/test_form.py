from pages.form_page import FormPage

class TestForm:

    def test_form(self, driver):
        form_page = FormPage(driver, 'http://users.bugred.ru/user/admin/index/')
        form_page.open()