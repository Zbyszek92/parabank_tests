from pages.login_page import LoginPage

def test_validation_button(driver):
    #1. Ładowanie strony
    login_page = LoginPage(driver)
    login_page.load()

    #2. Kliknięcie w button
    login_page.click_button_log()

    #3. Weryfikacja poprawnosci walidacji logowania przy braku danych
    error_validation_login = login_page.get_error_message()
    assert error_validation_login == "Please enter a username and password."




