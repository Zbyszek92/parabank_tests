import time
import random
from faker import Faker
from pages.register_page import RegisterPage

def test_success_register(register_page):

#1. Generowanie polski danych przez Faker
    fake = Faker("pl_PL")

#2. Generowanie unikalnego loginu i losowanie imienia i nazwiska   
    f_username = f"user_{random.randint(100, 999)}_{int(time.time())}"
    f_firstname = fake.first_name()
    f_lastname = fake.last_name()
    
#3. Akcje na stronie
    register_page.login_register(
        f_firstname, f_lastname, "Ulica 1", "Miasto", "Wojewodztwo","00-000", "123456", "SSN", f_username, "Haslo123", "Haslo123")


    success_text = register_page.get_success_register()
    assert "Your account was created successfully" in success_text






