import time

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.INPUT_EMAIL_SINGIN).send_keys("7dazzlestar3bagautd@gmail.com")
        self.element_is_visible(self.locators.INPUT_PASSWORD_SINGIN).send_keys("12345qa")
        self.element_is_visible(self.locators.BUTTON_SINGIN).click()
        time.sleep(3)