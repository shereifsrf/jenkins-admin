pipeline {
    // docker agent with label 'docker-slave-demo'
    // image is from config/pipeline/python
    agent {
        docker {
            image '.config/pipeline/python'
            label 'docker-slave-demo'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}