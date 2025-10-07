pipeline {
    agent any

    environment {
        // Set workspace-local Poetry path
        POETRY_HOME = "${WORKSPACE}\\.poetry"
        PATH = "${POETRY_HOME}\\bin;${PATH}" // Add poetry to PATH
    }

    options {
        skipDefaultCheckout(true) // We'll do checkout manually
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                echo "🔄 Checking out repository..."
                checkout scm
            }
        }

        stage('Verify Python & Node.js') {
            steps {
                echo "===== Verifying Python & Node.js ====="
                bat 'python --version'
                bat 'node --version'
                bat 'npm --version'
            }
        }

        stage('Setup Poetry') {
            steps {
                echo "📦 Installing Poetry locally in workspace..."
                script {
                    def poetryDir = "${env.WORKSPACE}\\.poetry"
                    if (!fileExists(poetryDir)) {
                        bat """powershell -Command "Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile install-poetry.py" """
                        bat "python install-poetry.py --yes --path ${poetryDir}"
                        bat "del install-poetry.py"
                    } else {
                        echo "Poetry already exists in workspace."
                    }
                }
                echo "✅ Verifying Poetry..."
                bat ".\\.poetry\\bin\\poetry --version"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "🔧 Installing project dependencies with Poetry..."
                bat ".\\.poetry\\bin\\poetry install --no-root"
            }
        }

        stage('Run Tests') {
            steps {
                echo "🏃 Running Behave / Playwright tests..."
                bat ".\\.poetry\\bin\\poetry run behave -f allure_behave.formatter:AllureFormatter -o allure-results/"
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo "📊 Generating Allure report..."
                bat "allure generate allure-results -o allure-report --clean"
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo "🧹 Archiving test results..."
            archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
            junit 'allure-results/**/*.xml'
        }
        success {
            echo "✅ Build succeeded!"
            // Optional: email notification
        }
        failure {
            echo "❌ Build failed!"
            // Optional: email notification
        }
    }
}
