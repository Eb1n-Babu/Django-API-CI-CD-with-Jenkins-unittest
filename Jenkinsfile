pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Eb1n-Babu/Django-API-CI-CD-with-Jenkins-unittest.git'
            }
        }
        stage('Test') {
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                python manage.py test
                '''
            }
        }
        stage('Restart Container') {
            steps {
                sh '''
                docker stop todo-api || true
                docker rm todo-api || true
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