pipeline {
    agent any 

    stages {
        stage('Czyszczenie i Pobieranie') {
            steps {
                // Czyścimy stare śmieci, jeśli jakieś zostały
                deleteDir()
                // Pobieramy kod na nowo
                checkout scm
            }
        }
        stage('Przygotowanie systemu') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip chromium chromium-driver
                '''
            }
        }
        stage('Instalacja i Testy') {
            steps {
                sh '''
                    # Najpierw instalujemy (bezpieczniejsza wersja)
                    pip3 install -r requirements.txt --break-system-packages || pip install -r requirements.txt
                    
                    # Dopiero w NOWEJ LINII odpalamy testy
                    python3 -m pytest --headless
                '''
            }
        }
    }
}