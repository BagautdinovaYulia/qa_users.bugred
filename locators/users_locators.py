from selenium.webdriver.common.by import By


class UsersLocators:
    CELL_EMAIL = (By.PARTIAL_LINK_TEXT, "/html/body/div[3]/table/tbody/tr[1]/td[1]")
    BUTTON_VIEW_USER = (By.CLASS_NAME, "btn btn-success")
    BUTTON_DELETE_USER = (By.PARTIAL_LINK_TEXT, "Удалить")
    BUTTON_PRIVATE_AREA = (By.CLASS_NAME, "dropdown-toggle")
