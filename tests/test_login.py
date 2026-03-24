from pages.login_page import LoginPage

def test_invalid_login(driver):
    # 1. Przygotowanie strony 
    login_page = LoginPage(driver)
    login_page.load()
    
    # 2. Próba logowania złymi danymi 
    login_page.login("Adam", "nowakkkkk")
    
    # 3. Sprawdzenie wyniku - Asercja
    error_text = login_page.get_error_message()
    assert error_text == "The username and password could not be verified."
