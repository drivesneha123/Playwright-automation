# Project Setup - NHS DSPT BDD Automation Framework

This document contains detailed setup instructions for project setup.

- [Install Python 3.12.9](#1-install-python-3129)
- [Install Poetry](#2-install-poetry)
- [Setup Virtual Environment](#3-setup-virtual-environment)
- [Install Dependencies](#4-install-dependencies)
- [Install Playwright Browsers](#5-install-playwright-browsers)
- [Export Dependencies (Optional)](#6-export-dependencies-optional)
- [Verify Behave Version](#7-verify-behave-version)
- [VS Code Integration](#8-vs-code-integration)
- [Allure Setup](#9-allure-setup)
- [Required VS Code Extensions](#10-required-vs-code-extensions)
- [Pre-commit Hooks Setup](#11-pre-commit-hooks-setup)
- [Install Node.js & Prettier](#12-install-nodejs--prettier-required-for-pre-commit-hooks)

---

## 1. Install Python 3.12.9

- Download and install Python 3.12.9.
- During installation, check **“Add Python to PATH”**.
- Verify installation:

```
  python --version
```

## 2. Install Poetry

1. Install Poetry:

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

2. Verify installation:

```
poetry --version
```

3. initialize Project (skip if pyproject.toml exists):

```
poetry init
```

## 3. Setup Virtual Environment

```
poetry env info
```

```
poetry shell

```

```
poetry env info --path # optional

```

## 4. Install Dependencies

Install main dependencies:

```
poetry install
```

```
poetry add behave playwright allure-python-commons pytest
```

```
poetry add requests faker python-dotenv
```

Install development dependencies:

```
poetry add --dev black flake8 isort allure-behave
```

## 5. Install Playwright Browsers

```
poetry run playwright install
```

## 6. Export Dependencies (Optional)

```
poetry self add poetry-plugin-export
```

## 7. Verify Behave Version

```
poetry run behave --version
```

## 8. VS Code Integration

Press Ctrl+Shift+P → Python: Select Interpreter
Choose the Poetry virtual environment (poetry env info --path)

## 9. Allure Setup

1. Open PowerShell as Administrator
2. Install Chocolatey:

```
Set-ExecutionPolicy Bypass -Scope Process -Force; `[System.Net.ServicePointManager]::SecurityProtocol =`
  [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
  iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. Install Allure:

```
choco install allure
```

```
allure --version
```

## 10. Required VS Code Extensions

To work with this project in VS Code, please install the following extensions:

1. Python – Python language support.
2. Playwright Test for VSCode – Run and debug Playwright tests.
3. Generate Allure Report – Generate Allure test reports directly from VS Code.
4. Cucumber (Gherkin) Full Support – Gherkin syntax highlighting and autocomplete.
5. Behave VSC – Behave BDD support.
6. Behave Test Explorer – Run Behave tests from the VS Code test explorer.
7. Black Formatter → for Python
8. Prettier - Code Formatter → for Gherkin (.feature) and other file types

## 11. Pre-commit Hooks Setup

1. Install pre-commit:

```
poetry add --dev pre-commit
```

```
poetry run pre-commit install
```

```
poetry run pre-commit run --all-files # optional
```

## 12. Install Node.js & Prettier (required for pre-commit hooks):

1. Run PowerShell as Administrator
2. Verify installation
   Install Node.js (LTS version) via Chocolatey
   `choco install nodejs-lts -y`
3. Verify installation
   `node --version`
   `npm --version`
4. Install Prettier globally
   `npm install -g prettier`
5. Verify Prettier installation
   `prettier --version`
6. Optional: Update npm to the latest version
   `npm install -g npm@latest`
