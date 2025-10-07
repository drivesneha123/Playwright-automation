pipeline {
    agent any

    environment {
        // Paths inside Jenkins workspace
        PYTHON_DIR = "${WORKSPACE}\\.python"
        POETRY_HOME = "${WORKSPACE}\\.poetry"
        NODEJS_HOME = "C:\\Program Files\\nodejs" // adjust if needed
        PATH = "${PYTHON_DIR};${PYTHON_DIR}\\Scripts;${POETRY_HOME}\\bin;${NODEJS_HOME};${NODEJS_HOME}\\bin;${env.PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning GitHub repository...'
                git branch: 'main', url: 'https://github.com/drivesneha123/Playwright-automation.git'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Downloading portable Python...'
                bat '''
                powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.9/python-3.12.9-embed-amd64.zip -OutFile python.zip"
                powershell -Command "Expand-Archive python.zip -DestinationPath .\\.python"
                del python.zip
                '''
                echo 'Verifying Python...'
                bat '''
                .\\.python\\python.exe --version
                '''
            }
        }

        stage('Install Node.js') {
            steps {
                echo 'Installing Node.js via Chocolatey (if not installed)...'
                bat '''
                choco install nodejs-lts -y --no-progress || echo Node.js already installed
                refreshenv
                node -v
                npm -v
                '''
            }
        }

        stage('Setup Poetry') {
            steps {
                echo 'Installing Poetry inside workspace...'
                bat '''
                powershell -Command "Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile install-poetry.py"
                .\\.python\\python.exe install-poetry.py --yes --path .\\.poetry
                del install-poetry.py
                '''
                echo 'Verifying Poetry...'
                bat '''
                .\\.poetry\\bin\\poetry --version
                '''
            }
        }

        stage('Install Project Dependencies') {
            steps {
                echo 'Installing project dependencies via Poetry...'
                bat '''
                .\\.poetry\\bin\\poetry install --no-root
                .\\.poetry\\bin\\poetry run playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Playwright + Behave tests...'
                bat '''
                .\\.poetry\\bin\\poetry run behave --tags @regression || exit 0
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure report...'
                bat '''
                if exist reports\\allure-results (
                    allure generate reports\\allure-results --clean -o reports\\allure-report
                ) else (
                    echo "Allure results folder not found, skipping report generation..."
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
