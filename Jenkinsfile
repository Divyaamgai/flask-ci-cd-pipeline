pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from your Git repository and specify the branch
                git branch: 'main', url: 'https://github.com/Divyaamgai/flask-ci-cd-pipeline.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Create a virtual environment and install dependencies
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install --upgrade pip'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (ensure you have test cases in your repo)
                    sh './venv/bin/python -m unittest discover'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t flask-app .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy to your desired environment (Docker, Azure, etc.)
                    sh 'docker run -d -p 5000:5000 flask-app'
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }

        success {
            echo "Deployment successful!"
        }

        failure {
            echo "Pipeline failed. Please check logs!"
        }
    }
}
