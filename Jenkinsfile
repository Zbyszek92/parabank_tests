pipeline {
    agent any
    
    stages {
        stage('Pobieranie kodu') {
            steps {
                checkout scm
            }
        }
        stage('Instalacja bibliotek') {
            steps {
                // Instalujemy Selenium i Pytest wewnątrz Jenkinsa
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Uruchamianie testów') {
            steps {
                // Odpalamy testy w trybie headless (bez okna przeglądarki)
                sh 'python3 -m pytest --headless'
            }
        }
    }
    post {
        always {
            echo 'Koniec pracy, melduję wykonanie zadania!'
        }
    }
}