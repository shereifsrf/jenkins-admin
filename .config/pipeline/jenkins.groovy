pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    label 'docker-agent'
                    image '.config/pipeline/python'
                }
            }
            steps {
                echo 'Building...'
                sh '/usr/local/bin/python --version'
            }
        }
    }
}