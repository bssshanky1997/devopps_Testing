pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building..."
            }
        }

        stage('Run') {
            steps {
                sh 'python3 Test.py'
            }
        }
    }
}
