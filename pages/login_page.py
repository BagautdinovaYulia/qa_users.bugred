import time

from generator.generator import generated_person, generated_password
from locators.login_locators import LoginLocators, RegistrationLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    locators = RegistrationLocators()

    def fill_registration_fields(self):
        # person_info = next(generated_person())
        # name = person_info.name
        # email = person_info.email

        # password_info = next(generated_password())
        # password = password_info.password

        self.element_is_visible(self.locators.INPUT_NAME).send_keys("TestName")
        self.element_is_visible(self.locators.INPUT_EMAIL_SINGUP).send_keys("7dazzlestar3bagautd@gmail.com")
        password_field = self.elements_are_present(self.locators.INPUT_PASSWORD_SINGUP)[1]
        password_field.send_keys("12345qa")
        self.element_is_visible(self.locators.BUTTON_SINGUP).click()
        time.sleep(3)
        # return person_info.email


class LoginPage(BasePage):
    locators = LoginLocators()

    def fill_login_fields(self):
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        time.sleep(3)
        self.element_is_visible(self.locators.INPUT_EMAIL_SINGIN).send_keys("7dazzlestar3bagautd@gmail.com")
        self.elements_are_present(self.locators.INPUT_PASSWORD_SINGIN).send_keys("12345qa")
        self.element_is_visible(self.locators.BUTTON_SINGIN).click()
        time.sleep(3)
