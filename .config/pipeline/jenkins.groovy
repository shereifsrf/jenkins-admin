pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    label 'docker-agent'
                }
            }
            steps {
                echo 'Building...'
                sh '/usr/local/bin/python --version'
            }
        }
    }
}