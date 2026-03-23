pipeline {
    // Mówimy Jenkinsowi: "Użyj obrazu Pythona jako swojego środowiska"
    agent {
        docker { 
            image 'python:3.10-slim' 
        }
    }
    
    stages {
        stage('Instalacja bibliotek') {
            steps {
                // Teraz pip na pewno będzie dostępny, bo jesteśmy w kontenerze Pythona
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Uruchamianie testów') {
            steps {
                // Instalujemy Chromium, bo sam Python go nie ma
                sh '''
                    apt-get update && apt-get install -y chromium chromium-driver
                    python3 -m pytest --headless
                '''
            }
        }
    }
}