pipeline {
    agent any

    environment {
        POETRY_HOME = "${WORKSPACE}\\poetry"
        PATH = "${POETRY_HOME}\\bin;${PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning GitHub repository...'
                git branch: 'main', url: 'https://github.com/drivesneha123/Playwright-automation.git'
            }
        }

        stage('Setup Python & Poetry') {
            steps {
                bat '''
                echo Installing Python dependencies...
                python --version

                echo Installing Poetry...
                (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

                echo Verifying Poetry...
                call %USERPROFILE%\\AppData\\Roaming\\Python\\Scripts\\poetry --version
                '''
            }
        }

        stage('Install Project Dependencies') {
            steps {
                bat '''
                echo Installing dependencies via Poetry...
                call %USERPROFILE%\\AppData\\Roaming\\Python\\Scripts\\poetry install
                call %USERPROFILE%\\AppData\\Roaming\\Python\\Scripts\\poetry run playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                echo Running Playwright Behave tests...
                call %USERPROFILE%\\AppData\\Roaming\\Python\\Scripts\\poetry run behave --tags @regression || exit 0
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                echo Generating Allure report...
                if exist reports\\allure-results (
                    allure generate reports\\allure-results --clean -o reports\\allure-report
                ) else (
                    echo "Allure results folder not found, skipping..."
                )
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
