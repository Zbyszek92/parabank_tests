from pages.login_page import LoginPage

def test_invalid_login(login_page):

    # 2. Próba logowania złymi danymi 
    login_page.login("Adamek", "nowakkkkk333")
    
    # 3. Sprawdzenie wyniku - Asercja
    error_text = login_page.get_error_message()
    assert error_text == "An internal error has occurred and has been logged."



  
