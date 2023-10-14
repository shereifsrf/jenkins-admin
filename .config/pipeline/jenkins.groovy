pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                // python 3.12.0 image
                docker {
                    image 'python:3.12.0'
                }
                steps {
                    sh 'python --version'
                }
            }
        }
    }
}