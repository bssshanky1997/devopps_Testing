pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

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
                bat 'python Test.py'
            }
        }
    }
}
