
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME     = 'devopsflow-cicd'
        IMAGE_TAG      = 'v1'
        CONTAINER_NAME = 'devopsflow-app'
        APP_PORT       = '5000'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out application source code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    py -3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat '''
                    py -3 -m pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    docker build -t %IMAGE_NAME%:%IMAGE_TAG% .
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                    docker rm -f %CONTAINER_NAME% 2>NUL
                    docker run -d --restart unless-stopped --name %CONTAINER_NAME% -p %APP_PORT%:5000 %IMAGE_NAME%:%IMAGE_TAG%
                '''
            }
        }

        stage('Application Health Check') {
            steps {
                bat '''
                    powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference='Stop'; for ($i=0; $i -lt 10; $i++) { try { $r=Invoke-RestMethod 'http://localhost:5000/health'; if ($r.status -eq 'healthy') { Write-Output 'Application health check passed'; exit 0 } } catch {}; Start-Sleep -Seconds 2 }; Write-Error 'Health check failed'; exit 1"
                '''
            }
        }
    }

    post {
        success {
            echo 'DevOpsFlow CI/CD Pipeline completed successfully.'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the stage logs.'
        }
    }
}
