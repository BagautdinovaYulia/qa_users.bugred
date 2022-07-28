import time

from pages.base_page import BasePage
from locators.users_locators import UsersLocators

class UsersPage(BasePage):

    locators = UsersLocators()

    def delete_user(self):
        self.element_is_present(self.locators.BUTTON_DELETE_USER).click()

    def check_added_user(self):
        assert self.element_is_visible(self.locators.BUTTON_DELETE_USER) is not None

    def check_deleted_user(self):
        assert self.element_is_visible(self.locators.BUTTON_DELETE_USER) is None
