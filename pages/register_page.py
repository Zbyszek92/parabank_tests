from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    # --- LOKALIZATORY ---
    REGISTER_BUTTON = (By.LINK_TEXT,"Register")
    FIRST_NAME = (By.NAME,"customer.firstName")
    LAST_NAME = (By.NAME,"customer.lastName")
    ADDRESS = (By.NAME, "customer.address.street")
    CITY = (By.NAME,"customer.address.city")
    STATE = (By.NAME,"customer.address.state")
    ZIP_CODE = (By.NAME,"customer.address.zipCode")
    PHONE = (By.NAME,"customer.phoneNumber")
    SSN_NUMBER = (By.NAME,"customer.ssn")
    USERNAME = (By.NAME,"customer.username")
    PASSWORD = (By.NAME,"customer.password")
    CONFIRM_PASSWORD = (By.NAME,"repeatedPassword")
    REGISTER_SUBMIT = (By.XPATH, "//input[@value='Register']")
    SUCCESS_PAGE = (By.XPATH, "//p[text()='Your account was created successfully. You are now logged in.']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://parabank.parasoft.com/parabank/index.htm"


    def login_register(self, firstname, lastname, address, city, state, zipcode, phone, ssn, username, password, confirmpassword):
        self.click(self.REGISTER_BUTTON)
        self.enter_text(self.FIRST_NAME, firstname)
        self.enter_text(self.LAST_NAME,lastname)
        self.enter_text(self.ADDRESS, address)
        self.enter_text(self.CITY, city)
        self.enter_text(self.STATE,state)
        self.enter_text(self.ZIP_CODE, zipcode)
        self.enter_text(self.PHONE, phone)
        self.enter_text(self.SSN_NUMBER, ssn)
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD,password)
        self.enter_text(self.CONFIRM_PASSWORD, confirmpassword)
        self.click(self.REGISTER_SUBMIT)

    def get_success_register(self):
        return self.get_text(self.SUCCESS_PAGE)


    

    






