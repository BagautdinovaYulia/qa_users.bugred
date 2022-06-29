import random

from selenium.webdriver.common.by import By


class FormLocators:
    INPUT_NAME = (By.NAME, "noibiz_name")
    INPUT_EMAIL = (By.NAME, "noibiz_email")
    INPUT_PASSWORD = (By.NAME, "noibiz_password")
    # AVATAR
    # DATE
    # MALE
    BUTTON_ADD_USER = (By.NAME, "act_create")
