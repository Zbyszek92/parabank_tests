# ParaBank UI Automation Framework

Projekt demonstracyjny przedstawiający w pełni zautomatyzowane środowisko do testów UI aplikacji bankowej [ParaBank](https://parabank.parasoft.com/). 

## Wykorzystane Technologie

* **Język:** Python 3
* **Automatyzacja UI:** Selenium WebDriver
* **Silnik testowy:** Pytest
* **Wzorzec Projektowy:** Page Object Model (POM) ze wspólną klasą `BasePage`
* **Zarządzanie Zależnościami:** Wirtualne środowisko (`venv`), `pip`
* **CI/CD & Infrastruktura:** Jenkins Pipeline, Docker
* **Kontrola Wersji:** Git / GitHub

## Główne Cechy Projektu

1. **Architektura Page Object Model:** Logika stron (lokatory, metody) jest całkowicie odseparowana od logiki testów. 
2. **Dynamiczne Generowanie Danych (TDM):** Skrypty testowe samodzielnie generują unikalne dane (np. loginy z użyciem znaczników czasu).
3. **Pipeline jako Kod (Jenkinsfile):** Cały proces pobierania kodu, instalacji zależności (w tym przeglądarki Chrome w trybie headless) i uruchamiania testów jest opisany w pliku konfiguracyjnym. 

## Struktura Projektu

```text
parabank_tests/
├── pages/
│   ├── __init__.py
│   ├── base_page.py        # Główne metody "wrappery" (np. WebDriverWait, find_element)
│   ├── login_page.py       # Lokatory i akcje dla strony logowania
│   └── register_page.py    # Lokatory i akcje dla formularza rejestracji
├── tests/
│   ├── __init__.py
│   ├── conftest.py         # Konfiguracja WebDrivera, opcje Chrome i globalne fixtury
│   ├── test_login.py       # Scenariusze testowe dla procesu logowania
│   ├── test_register.py    # Scenariusze testowe dla rejestracji użytkownika
│   └── test_validation.py  # Testy weryfikujące komunikaty walidacyjne
├── Jenkinsfile             # Skrypt potoku CI/CD
├── pytest.ini              # Konfiguracja silnika Pytest 
└── requirements.txt        # Zablokowane wersje używanych bibliotek (pip)
```

<video src="assets/screen_recording.mov" controls="controls" width="100%"></video>