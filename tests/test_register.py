import time

from pages.register_page import Register_page

def test_success_register(driver):
    # 1 Przygotowanie strony 
    login = Register_page(driver)
    login.load()

    # 2. GENEROWANIE UNIKALNEGO LOGINU
    unique_username = f"adam_{int(time.time())}"
    
    print(f"Rejestruje uzytkownika z loginem: {unique_username}")

    # 2 Akcja rejestracji na stronie przez uzytkownika
    login.login_register("Adas", "Sroka","Testowa 40","Warsaw","Polska", "05-074","111111111", "4321", unique_username, "Testowa1234!","Testowa1234!")

    # 3 Sprawdzenie poprawności logowania
    succes = login.get_success_register()
    assert succes == "Your account was created successfully. You are now logged in."

    




