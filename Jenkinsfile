// pipeline {
//     agent any

//     environment {
//         PYTHON_VERSION = '3.9'
//         DOCKER_PATH = '/usr/local/bin:$PATH'  // Ensure Docker is in the path
//     }

//     stages {
//         stage('Check Docker Version') {
//             steps {
//                 script {
//                     sh 'echo $PATH'
//                     sh 'docker --version'
//                 }
//             }
//         }

//         stage('Checkout') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/Divyaamgai/flask-ci-cd-pipeline.git'
//             }
//         }

//         stage('Set up Python Environment') {
//             steps {
//                 script {
//                     sh 'python3 -m venv venv'
//                     sh './venv/bin/pip install --upgrade pip'
//                     sh './venv/bin/pip install -r requirements.txt'
//                 }
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 script {
//                     sh './venv/bin/python -m unittest discover'
//                 }
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     sh 'docker build -t flask-app .'
//                 }
//             }
//         }

//         stage('Deploy') {
//             steps {
//                 script {
//                     echo "Stopping any existing containers on port 5000"
//                     sh '''
//                         docker ps --filter "publish=5000" -q | xargs -r docker stop || true
//                         docker ps -a --filter "publish=5000" -q | xargs -r docker rm || true
//                     '''
//                     echo "Running new container on port 5000"
//                     sh 'docker run -d -p 5000:5000 flask-app'
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             cleanWs()
//         }

//         success {
//             echo "Deployment successful!"
//         }

//         failure {
//             echo "Pipeline failed. Please check logs!"
//         }
//     }
// }

pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
        DOCKER_PATH = '/usr/local/bin:$PATH'  // Ensure Docker is in the path
    }

    stages {
        stage('Check Docker Version') {
            steps {
                script {
                    sh 'echo $PATH'
                    sh 'docker --version'
                }
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Divyaamgai/flask-ci-cd-pipeline.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install --upgrade pip'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh './venv/bin/python -m unittest discover'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flask-app .'
                }
            }
        }

        stage('Trivy Scan') {
            steps {
                script {
                    echo "Running Trivy vulnerability scan..."
                    // Run scan and fail build if HIGH or CRITICAL issues found
                    sh 'trivy image --exit-code 1 --severity HIGH,CRITICAL flask-app'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Stopping any existing containers on port 5000"
                    sh '''
                        docker ps --filter "publish=5000" -q | xargs -r docker stop || true
                        docker ps -a --filter "publish=5000" -q | xargs -r docker rm || true
                    '''
                    echo "Running new container on port 5000"
                    sh 'docker run -d -p 5000:5000 flask-app'
                }
            }
        }
    }

    post {
        always {
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
