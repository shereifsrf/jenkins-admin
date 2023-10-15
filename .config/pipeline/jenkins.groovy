pipeline {
    agent {
        // use the dockerfile from .config/python/Dockerfile
        dockerfile {
            filename '.config/python/Dockerfile'
        }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '/usr/local/bin/python --version'
            }
        }
    }
}