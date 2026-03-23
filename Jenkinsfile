pipeline {
    agent any 

    stages {
        stage('Przygotowanie systemu') {
            steps {
                // Instalujemy wszystko, czego Jenkinsowi brakuje do życia
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip chromium chromium-driver
                '''
            }
        }
        stage('Instalacja bibliotek Pythona') {
            steps {
                // Instalujemy Selenium i Pytest
                // Flaga --break-system-packages pozwala obejść blokady w nowszych systemach
                sh 'pip3 install -r requirements.txt --break-system-packages || pip install -r requirements.txt'
            }
        }
        stage('Uruchamianie testów') {
            steps {
                // Odpalamy testy w trybie headless
                sh 'python3 -m pytest --headless'
            }
        }
    }
    post {
        always {
            echo 'Praca zakończona. Sprawdź logi powyżej!'
        }
    }
}