pipeline {
    // docker agent with label 'docker-slave-demo'
    // image is from config/pipeline/python
    agent {
        docker {
            // Specify the Dockerfile path here
            image 'ubuntu-tester'
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