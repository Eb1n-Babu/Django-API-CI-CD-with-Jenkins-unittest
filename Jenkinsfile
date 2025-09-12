pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'  // Replace with your repo
            }
        }
        stage('Lint') {
            steps {
                sh 'python -m pylint tasks/ todo_api/'
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
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-todo-api:$BUILD_NUMBER .'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                docker stop django-todo-api || true
                docker rm django-todo-api || true
                docker run -d --name django-todo-api -p 8000:8000 django-todo-api:$BUILD_NUMBER
                '''
            }
        }
    }
    post {
        always {
            cleanWs()  // Clean workspace
        }
    }
}