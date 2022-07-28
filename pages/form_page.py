import time
from generator.generator import generated_person, generated_password
from locators.form_locators import FormLocators
from locators.users_locators import UsersLocators
from pages.base_page import BasePage

class FormPage(BasePage):
    locators = FormLocators()
    locator_check = UsersLocators()

    def fill_form_fields(self):
        person_info = next(generated_person())
        name = person_info.name
        email = person_info.email

        password_info = next(generated_password())
        password = password_info.password

        self.element_is_visible(self.locators.BUTTON_ADD_USER).click()
        time.sleep(3)
        self.element_is_visible(self.locators.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.BUTTON_ADD_USER, timeout=5).click()

