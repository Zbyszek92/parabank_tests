from pages.login_page import LoginPage

def test_invalid_login(driver):
    # 1. Przygotowanie strony (Arrange)
    login_page = LoginPage(driver)
    login_page.load()
    
    # 2. Akcja - próba logowania złymi danymi (Act)
    login_page.login("testowy_user", "zle_haslo")
    
    # 3. Sprawdzenie wyniku - Asercja (Assert)
    error_text = login_page.get_error_message()
    assert error_text == "The username and password could not be verified.", \
        f"Oczekiwano innego błędu. Otrzymano: {error_text}"
