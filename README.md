# NHS DSPT - BDD Automation Framework (Python + Playwright + Behave)

This is a BDD automation framework developed using Playwright and Python Behave.

The goal of this framework is to enable **readable**, **maintainable**, and **scalable** automation by combining:
BDD feature files, modular page objects, custom logging, and rich reporting with Allure.

## Project Structure

**features/**

- `steps/` → contains all step definition files
- `.feature` files → contain BDD test scenarios

**Pages/**

- elements and corresponding actions of the pages

**utils/**

- `custom_logger.py` → reusable logging utility (logs to console + `logs/dspt.log`)
- `tag_helper.py` → utilities for extracting values from Gherkin tags

**helpers/**

- `browser_instance.py` → manages Playwright browser launch/closure
- `playwright_helpers.py` → reusable Playwright helper functions (click, fill, visibility, file upload, etc.)

**logs/** → execution logs

**screenshots/** → screenshots captured automatically on failure

**data/** → JSON files with reusable test data (organisation codes, outcome titles, descriptions, etc.)

**.env** → environment variables like BASE_URL, BROWSER, HEADLESS, credentials

**Visual Studio code** → is used as IDE.

## Commands to run Tests

**To run the test with allure report**

`poetry run behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results ./features/<feature-file_name>.feature`

**To generate the html allure report from the json files inside Reports folder**

`allure generate reports/allure-results -o reports/allure-report --clean`

**Open report in browser**

`allure open reports/allure-report`

**To run without allure**

`poetry run behave .\features\<feature_file_name>.feature`

## Quick Start

For detailed setup instructions, see [SETUP.md](SETUP.md)

1. Clone the repo:
   `git clone <repo-url>`
   `cd <repo-folder>`

2. Install Python dependencies with Poetry:
   `poetry install`

3. Activate the virtual environment:
   `poetry shell`
