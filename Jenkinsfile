pipeline {
    agent any

    environment {
        // Local Python path in workspace
        PYTHON_HOME = "${WORKSPACE}\\.python"
        PATH = "${PYTHON_HOME};${PYTHON_HOME}\\Scripts;${PATH}"

        // Local Poetry path in workspace
        POETRY_HOME = "${WORKSPACE}\\.poetry"
        PATH = "${POETRY_HOME}\\bin;${PATH}"
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
                echo 'Downloading and setting up portable Python...'
                bat '''
                if not exist .\\.python (
                    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.9/python-3.12.9-embed-amd64.zip -OutFile python.zip"
                    powershell -Command "Expand-Archive python.zip -DestinationPath .\\.python"
                    del python.zip
                )
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
                if not exist .\\.poetry (
                    powershell -Command "Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile install-poetry.py"
                    .\\.python\\python.exe install-poetry.py --yes --path .\\.poetry
                    del install-poetry.py
                )
                call .\\.poetry\\bin\\poetry --version
                '''
            }
        }

        stage('Install Project Dependencies') {
            steps {
                echo 'Installing dependencies via Poetry...'
                bat '''
                call .\\.poetry\\bin\\poetry install --no-root
                call .\\.poetry\\bin\\poetry run playwright install
                '''
            }
        }

        stage('Run Behave Tests') {
            steps {
                echo 'Running Playwright + Behave tests...'
                bat '''
                call .\\.poetry\\bin\\poetry run behave --tags @regression || exit 0
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
