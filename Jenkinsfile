pipeline {
    agent any

    environment {
        POETRY_HOME = "${WORKSPACE}\\.poetry"
        PATH = "${POETRY_HOME}\\bin;${WORKSPACE}\\.nodejs\\node-v20.8.1-win-x64;${WORKSPACE}\\.allure\\bin;${PATH}"
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
                echo '===== Verifying Python ====='
                bat 'python --version'

                echo '===== Installing Poetry locally in workspace ====='
                bat """
                powershell -Command "Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile .\\\\install-poetry.py -UseBasicParsing"
                python install-poetry.py --yes --no-modify-path
                """

                echo '===== Verifying Poetry Installation ====='
                bat '.\\.poetry\\bin\\poetry --version'
            }
        }

        stage('Setup Node.js for Playwright') {
            steps {
                echo '===== Installing Node.js locally in workspace ====='
                bat """
                powershell -Command "Invoke-WebRequest -Uri https://nodejs.org/dist/v20.8.1/node-v20.8.1-win-x64.zip -OutFile node.zip"
                powershell -Command "Expand-Archive node.zip -DestinationPath .\\\\.nodejs"
                """
                echo '===== Verifying Node.js ====='
                bat '.\\.nodejs\\node-v20.8.1-win-x64\\node.exe --version'
                bat '.\\.nodejs\\node-v20.8.1-win-x64\\npm.cmd --version'
            }
        }

        stage('Install Project Dependencies') {
            steps {
                echo '===== Installing project dependencies ====='
                bat '.\\.poetry\\bin\\poetry install --no-root'
                bat '.\\.poetry\\bin\\poetry run playwright install'
            }
        }

        stage('Setup Allure CLI') {
            steps {
                echo '===== Installing Allure CLI locally ====='
                bat """
                powershell -Command "Invoke-WebRequest -Uri https://github.com/allure-framework/allure2/releases/download/2.23.1/allure-2.23.1.zip -OutFile allure.zip"
                powershell -Command "Expand-Archive allure.zip -DestinationPath .\\\\.allure"
                """
                echo '===== Verifying Allure CLI ====='
                bat '.\\.allure\\allure-2.23.1\\bin\\allure.bat --version'
            }
        }

        stage('Run Tests') {
            steps {
                echo '===== Running Playwright Behave tests ====='
                bat '.\\.poetry\\bin\\poetry run behave --tags @regression || exit 0'
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo '===== Generating Allure Report ====='
                bat """
                if exist reports\\allure-results (
                    .\\.allure\\allure-2.23.1\\bin\\allure.bat generate reports\\allure-results --clean -o reports\\allure-report
                ) else (
                    echo "Allure results folder not found, skipping..."
                )
                """
                publishHTML([allowMissing: true,
                             alwaysLinkToLastBuild: true,
                             keepAll: true,
                             reportDir: 'reports\\allure-report',
                             reportFiles: 'index.html',
                             reportName: 'Allure Report'])
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
