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
                bat '''
                py -3 --version
                if not exist .venv (
                    py -3 -m venv .venv
                )
                .venv\\Scripts\\python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run') {
            steps {
                bat '.venv\\Scripts\\python Test.py'
            }
        }
    }
}
