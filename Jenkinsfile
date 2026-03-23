pipeline {
    agent any 

    stages {
        stage('Czyszczenie i Pobieranie') {
            steps {
                deleteDir()
                checkout scm
            }
        }
        stage('Przygotowanie systemu') {
            steps {
                sh '''
                    apt-get update
                    # Dodajemy python3-venv, który jest kluczowy!
                    apt-get install -y python3 python3-pip python3-venv chromium chromium-driver
                '''
            }
        }
        stage('Instalacja i Testy') {
            steps {
                sh '''
                    # 1. Tworzymy wirtualne środowisko w folderze 'jenkins_venv'
                    python3 -m venv jenkins_venv
                    
                    # 2. Instalujemy biblioteki używając pip-a z tego środowiska
                    ./jenkins_venv/bin/pip install --upgrade pip
                    ./jenkins_venv/bin/pip install -r requirements.txt
                    
                    # 3. Odpalamy testy używając Pythona z tego środowiska
                    ./jenkins_venv/bin/python -m pytest --headless
                '''
            }
        }
    }
}