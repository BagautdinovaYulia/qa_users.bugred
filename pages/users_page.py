import time

from pages.base_page import BasePage
from locators.users_locators import UsersLocators

class UsersPage(BasePage):

    locators = UsersLocators()

    # def check_new_user(self):

    def delete_user(self):
        self.element_is_present(self.locators.BUTTON_DELETE_USER).click()

    # кнопка "Успешно удалено!" пропадает за 1 сек
    # def check_deleted_user(self):
