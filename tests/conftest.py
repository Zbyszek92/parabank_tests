import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Uruchom w trybie headless")

@pytest.fixture()
def driver(request):
   
    options = Options()
    options.add_argument("--incognito")
    
    if request.config.getoption("--headless"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    if os.path.exists("/usr/bin/chromedriver"):
        service = Service("/usr/bin/chromedriver")
    else:
        service = Service(ChromeDriverManager().install())
        
    driver = webdriver.Chrome(service=service, options=options)
    
    if not request.config.getoption("--headless"):
        driver.maximize_window()
        
    yield driver
    driver.quit()