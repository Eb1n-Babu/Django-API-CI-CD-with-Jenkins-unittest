pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                bat 'git checkout main || git checkout -b main'
                git branch: 'main', url: 'https://github.com/Eb1n-Babu/Django-API-CI-CD-with-Jenkins-unittest.git'
            }
        }
        stage('Test') {
            steps {
                bat '''
                "C:\\Users\\ebinb\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                C:\\Users\\ebinb\\AppData\\Local\\Programs\\Python\\Python313\\python.exe manage.py test
                '''
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat '''
                    echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                    '''
                }
            }
        }
        stage('Restart Container') {
            steps {
                bat '''
                docker stop todo-api || exit 0
                docker rm todo-api || exit 0
                docker pull todo-api:latest
                docker run -d --name todo-api -p 8000:8000 todo-api:latest
                '''
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}