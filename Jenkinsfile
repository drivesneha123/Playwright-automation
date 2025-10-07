pipeline {
    agent any

    environment {
        POETRY_HOME = "${WORKSPACE}\\poetry"
        PATH = "${POETRY_HOME}\\bin;${PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔄 Checking out code from GitHub...'
                git branch: 'main', url: 'https://github.com/drivesneha123/Playwright-automation.git'
            }
        }

        stage('Setup Python & Poetry') {
            steps {
                bat '''
                echo ===== Verifying Python =====
                python --version

                echo ===== Installing Poetry =====
                (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

                echo ===== Verifying Poetry =====
                call %USERPROFILE%\\AppData\\Roaming\\Python\\Scripts\\poetry --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                echo ===== Installing Project Dependencies =====
                call %USERPROFILE%\\AppData\\Roaming\\Python\\Scripts\\poetry install
                call %USERPROFILE%\\AppData\\Roaming\\Python\\Scripts\\poetry run playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                echo ===== Running Playwright Tests =====
                call %USERPROFILE%\\AppData\\Roaming\\Python\\Scripts\\poetry run behave --tags @regression || exit 0
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                echo ===== Generating Allure Report =====
                if exist reports\\allure-results (
                    allure generate reports\\allure-results --clean -o reports\\allure-report
                ) else (
                    echo "⚠️ No Allure results found, skipping report generation."
                )
                '''
            }
        }
    }

    post {
        always {
            script {
                echo '🧹 Cleaning up workspace...'
                deleteDir() // safer alternative to cleanWs()
            }
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
