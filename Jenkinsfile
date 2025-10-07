pipeline {
    agent any

    environment {
        POETRY_HOME = "${WORKSPACE}\\poetry"
        PATH = "${POETRY_HOME}\\bin;${env:PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                echo '📦 Cloning GitHub repository...'
                git branch: 'main', url: 'https://github.com/drivesneha123/Playwright-automation.git'
            }
        }

        stage('Setup Python & Poetry') {
            steps {
                echo '🐍 Setting up Python and Poetry...'

                // ✅ Run PowerShell for Poetry installation
                powershell '''
                    Write-Host "Python version:"
                    python --version

                    Write-Host "Installing Poetry..."
                    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

                    # Add Poetry to PATH for this session
                    $env:Path += ";$env:APPDATA\\Python\\Scripts"

                    Write-Host "Verifying Poetry..."
                    poetry --version

                    # Configure Poetry to create virtualenv inside project
                    poetry config virtualenvs.in-project true
                '''
            }
        }

        stage('Install Project Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                powershell '''
                    $env:Path += ";$env:APPDATA\\Python\\Scripts"
                    poetry install
                    poetry run playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running Playwright Behave tests...'
                powershell '''
                    $env:Path += ";$env:APPDATA\\Python\\Scripts"
                    poetry run behave
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo '📊 Generating Allure report...'
                powershell '''
                    if (Test-Path "reports\\allure-results") {
                        allure generate reports\\allure-results --clean -o reports\\allure-report
                    } else {
                        Write-Host "⚠️ Allure results folder not found, skipping..."
                    }
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up workspace...'
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
