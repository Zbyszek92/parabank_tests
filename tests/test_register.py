import time
import random
from faker import Faker
from pages.register_page import Register_page

def test_success_register(driver):
    login = Register_page(driver)
    login.load()

    fake = Faker("pl_PL")
    
    f_username = f"user_{random.randint(100, 999)}_{int(time.time())}"
    f_firstname = fake.first_name()
    f_lastname = fake.last_name()

    login.login_register(
        f_firstname, f_lastname, "Ulica 1", "Miasto", "Wojewodztwo","00-000", "123456", "SSN", f_username, "Haslo123", "Haslo123")

    time.sleep(1)
    success_text = login.get_success_register()
    assert "Your account was created successfully" in success_text






