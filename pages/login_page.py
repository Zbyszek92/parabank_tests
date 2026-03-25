from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # --- LOKALIZATORY ---
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.button[value='Log In']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.error")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://parabank.parasoft.com/parabank/index.htm"

    # --- AKCJE NA STRONIE ---

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def click_button_log(self):
        self.click(self.LOGIN_BUTTON)
        
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)