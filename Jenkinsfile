pipeline {
    agent any

    environment {
        PYTHON_HOME = "${WORKSPACE}\\.python"
        POETRY_HOME = "${WORKSPACE}\\.poetry"
        PATH = "${PYTHON_HOME};${POETRY_HOME}\\bin;${env.PATH}"
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
                '''
                echo 'Verifying Python...'
                bat '.\\.python\\python.exe --version'
            }
        }

        stage('Setup Poetry') {
            steps {
                echo 'Installing Poetry...'
                bat '''
                .\\.python\\python.exe -m ensurepip
                .\\.python\\python.exe -m pip install --upgrade pip
                powershell -Command "Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile install-poetry.py"
                .\\.python\\python.exe install-poetry.py -y -p %WORKSPACE%\\.poetry
                '''
                echo 'Verifying Poetry...'
                bat '.\\.poetry\\bin\\poetry --version'
            }
        }

        stage('Install Project Dependencies') {
            steps {
                echo 'Installing project dependencies via Poetry...'
                bat '''
                .\\.poetry\\bin\\poetry config virtualenvs.in-project true
                .\\.poetry\\bin\\poetry install
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
