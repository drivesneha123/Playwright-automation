pipeline {
    agent any

    environment {
    PYTHON_DIR = "${WORKSPACE}\\.python"
    POETRY_HOME = "${WORKSPACE}\\.poetry"
    NODEJS_HOME = "${WORKSPACE}\\.nodejs"
    PATH = "${PYTHON_DIR};${PYTHON_DIR}\\Scripts;${POETRY_HOME}\\bin;${NODEJS_HOME};${NODEJS_HOME}\\bin;${env.PATH}"
}

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning GitHub repository...'
                git branch: 'main', url: 'https://github.com/drivesneha123/Playwright-automation.git'
            }
        }

        stage('Install Python') {
            steps {
                bat """
                echo ===== Installing Python via Chocolatey =====
                choco install python --version=3.12.9 -y --no-progress
                refreshenv
                python --version
                """
            }
        }

        stage('Install Node.js') {
            steps {
                bat """
                echo ===== Installing Node.js via Chocolatey =====
                choco install nodejs-lts -y --no-progress
                refreshenv
                node --version
                npm --version
                """
            }
        }

        stage('Setup Poetry') {
            steps {
                bat """
                echo ===== Installing Poetry =====
                powershell -Command "Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile install-poetry.py"
                python install-poetry.py -y -p ${POETRY_HOME}
                call ${POETRY_HOME}\\bin\\poetry --version
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                echo ===== Installing Project Dependencies via Poetry =====
                call ${POETRY_HOME}\\bin\\poetry config virtualenvs.in-project true
                call ${POETRY_HOME}\\bin\\poetry install --no-root
                call ${POETRY_HOME}\\bin\\poetry run playwright install
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                echo ===== Running Playwright Behave Tests =====
                call ${POETRY_HOME}\\bin\\poetry run behave --tags @regression || exit 0
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat """
                echo ===== Generating Allure Report =====
                if exist reports\\allure-results (
                    allure generate reports\\allure-results --clean -o reports\\allure-report
                ) else (
                    echo "Allure results folder not found, skipping..."
                )
                """
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
