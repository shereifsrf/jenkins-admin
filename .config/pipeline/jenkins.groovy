pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '/usr/local/bin/python --version'
            }
        }
    }
}