pipeline {
    agent none
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python --version'
            }
        }
    }
}