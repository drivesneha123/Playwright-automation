pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/drivesneha123/Playwright-automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                cd %WORKSPACE%
                (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
                poetry install
                poetry run playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                cd %WORKSPACE%
                poetry run behave
                '''
            }
        }
    }
}
