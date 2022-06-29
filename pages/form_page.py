import time
from generator.generator import generated_person
from locators.form_locators import FormLocators
from pages.base_page import BasePage

class FormPage(BasePage):
    locators = FormLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        self.element_is_visible(self.locators.INPUT_NAME).send_keys(person.name)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(person.password)
        self.element_is_visible(self.locators.BUTTON_ADD_USER).click()
        time.sleep(3)
        return person