pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
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