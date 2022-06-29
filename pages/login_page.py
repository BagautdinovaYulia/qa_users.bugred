import time

from generator.generator import generated_person
from locators.login_locators import LoginLocators, RegistrationLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.INPUT_EMAIL_SINGIN).send_keys("7dazzlestar3bagautd@gmail.com")
        self.element_is_visible(self.locators.INPUT_PASSWORD_SINGIN).send_keys("12345qa")
        self.element_is_visible(self.locators.BUTTON_SINGIN).click()
        time.sleep(3)

class RegistrationPage(BasePage):
    locators = RegistrationLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        name = person_info.name
        email = person_info.email
        password = person_info.password
        self.element_is_visible(self.locators.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.locators.INPUT_EMAIL_SINGUP).send_keys(email)
        self.element_is_visible(self.locators.INPUT_PASSWORD_SINGUP).send_keys(password)
        self.element_is_visible(self.locators.BUTTON_SINGUP).click()
        time.sleep(3)
        return person_info
