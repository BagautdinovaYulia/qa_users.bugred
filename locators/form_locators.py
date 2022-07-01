from selenium.webdriver.common.by import By


class FormLocators:
    BUTTON_USERS = (By.XPATH, "//*[@id='main-menu']/ul/li[1]/a/span")

    INPUT_NAME = (By.NAME, "noibiz_name")
    INPUT_EMAIL = (By.NAME, "noibiz_email")
    INPUT_PASSWORD = (By.NAME, "noibiz_password")
    # AVATAR
    # DATE
    # MALE
    BUTTON_ADD_USER = (By.NAME, "act_create")

    BUTTON_YOUR_ACCOUNT = (By.CLASS_NAME, "dropdown-toggle")
    BUTTON_LOGOUT = (By.LINK_TEXT, "Выход")


