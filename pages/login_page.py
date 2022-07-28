import time

from generator.generator import generated_person, generated_password
from locators.login_locators import LoginLocators, RegistrationLocators
from locators.users_locators import UsersLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    locators = RegistrationLocators()
    locator_check = UsersLocators()

    def fill_registration_fields(self):
        person_info = next(generated_person())
        name = person_info.name
        email = person_info.email

        password_info = next(generated_password())
        password = password_info.password

        self.element_is_visible(self.locators.INPUT_NAME).send_keys(name)
        self.element_is_visible(self.locators.INPUT_EMAIL_SINGUP).send_keys(email)
        password_field = self.elements_are_present(self.locators.INPUT_PASSWORD_SINGUP)[1]
        password_field.send_keys(password)
        self.element_is_visible(self.locators.BUTTON_SINGUP, timeout=5).click()

        return email, password

    def check_registration(self):
        assert self.element_is_visible(self.locator_check.BUTTON_PRIVATE_AREA) is not None


class LoginPage(BasePage, RegistrationPage):
    locators = LoginLocators()

    def fill_login_fields(self, email, password):
        # email = RegistrationPage.fill_registration_fields.email
        # password = RegistrationPage.fill_registration_fields.password

        self.element_is_visible(self.locators.INPUT_EMAIL_SINGIN).send_keys(email)
        self.elements_are_present(self.locators.INPUT_PASSWORD_SINGIN).send_keys(password)
        self.element_is_visible(self.locators.BUTTON_SINGIN, timeout=5).click()

