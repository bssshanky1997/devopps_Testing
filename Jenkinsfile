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
                bat 'py -3 --version'
                bat 'py -3 -m pip install -r requirements.txt'
            }
        }

        stage('Run') {
            steps {
                bat 'py -3 Test.py'
            }
        }
    }
}
