from selenium.webdriver.common.by import By


class LoginLocators:

    BUTTON_LOGIN = (By.XPATH, "//*[@id='main-menu']/ul/li[2]/a/span")

    INPUT_EMAIL_SINGIN = (By.NAME, "login")
    INPUT_PASSWORD_SINGIN = (By.NAME, "password")
    BUTTON_SINGIN = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input")

class RegistrationLocators:

    INPUT_NAME = (By.NAME, "name")
    INPUT_EMAIL_SINGUP = (By.NAME, "email")
    INPUT_PASSWORD_SINGUP = (By.NAME, "password")
    BUTTON_SINGUP = (By.NAME, "act_register_now")


#elements = driver.find_elements(driver, locator)
#elemt1 = elements[0]