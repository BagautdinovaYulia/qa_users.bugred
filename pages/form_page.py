import time
from generator.generator import generated_person, generated_password
from locators.form_locators import FormLocators
from pages.base_page import BasePage

class FormPage(BasePage):
    locators = FormLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        name = person.name
        email = person.email

        password = next(generated_password())
        password = password.password

        self.element_is_visible(self.locators.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.BUTTON_ADD_USER).click()
        time.sleep(3)
        return person.email

    # def open_form(self):
    #    self.element_is_visible(self.locators.BUTTON_USERS).click()
    #    time.sleep(3)