from helpers.browser_instance import BrowserManager
from utils.custom_logger import logger
from helpers.credentials_helper import get_credentials
from allure_commons.types import AttachmentType
import allure
import os
import traceback
import json


def _attach_console_logger(page):
    def log_console(msg):
        if msg.type != "info":
            logger.info(f"[Browser Console] {msg.type}: {msg.text}")

    page.on("console", log_console)


def load_credentials():
    """Load credentials from JSON file."""
    with open("data/credentials.json") as f:
        return json.load(f)


def before_all(context):
    logger.info("=== Test Run Started ===")
    os.makedirs("screenshots", exist_ok=True)


def before_feature(context, feature):
    logger.info(f"Starting feature: {feature.name}")

    # Launch browser and context ONCE per feature
    if "E2ERegression" in feature.tags:
        # Launch once per feature using BrowserManager
        context.browser = BrowserManager.launch_browser()
        context.playwright = BrowserManager._playwright
        context.context = context.browser.new_context()
        context.page = context.context.new_page()
        _attach_console_logger(context.page)
        context.shared_browser = True
    else:
        context.shared_browser = False
        context.page = None


def before_scenario(context, scenario):
    logger.info(f"Starting scenario: {scenario.name}")
    if not context.shared_browser:
        # Launch fresh browser for each scenario using BrowserManager
        context.browser = BrowserManager.launch_browser()
        context.playwright = BrowserManager._playwright
        context.context = context.browser.new_context()
        context.page = context.context.new_page()
        _attach_console_logger(context.page)

    # Load credentials
    creds_json = load_credentials()
    context.credentials, source, role = get_credentials(scenario, creds_json)
    logger.info(f"[{source}] Loaded credentials for role: {role}")


def after_step(context, step):
    if step.status == "failed":
        logger.error(f"Step FAILED: {step.keyword} {step.name}")
        # Capture full traceback
        error_trace = traceback.format_exc()
        allure.attach(
            error_trace, name="Stack Trace", attachment_type=AttachmentType.TEXT
        )

        # Capture screenshot
        # Ensure step name is safe for filenames
        safe_step_name = (
            step.name.replace(" ", "_")
            .replace("/", "_")
            .replace('"', "")
            .replace("'", "")
            .replace(":", "_")
        )
        screenshot_path = f"screenshots/{safe_step_name}_step.png"

        try:
            if hasattr(context, "page") and context.page:
                # Save screenshot to file
                context.page.screenshot(path=screenshot_path)

                # Attach screenshot to Allure
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=f"Failed Step - {step.name}",
                        attachment_type=AttachmentType.PNG,
                    )
            else:
                print("No active page found for screenshot.")
        except Exception as e:
            print(f"Screenshot capture failed: {e}")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        logger.error(f"Scenario FAILED: {scenario.name}")
    else:
        logger.info(f"Scenario PASSED: {scenario.name}")
    if not context.shared_browser:
        # Close browser after each scenario
        context.page.close()
        context.context.close()
        context.browser.close()
        context.playwright.stop()


def after_feature(context, feature):
    logger.info(f"Finished feature: {feature.name}")
    if getattr(context, "shared_browser", False):
        if hasattr(context, "page") and context.page:
            context.page.close()
        if hasattr(context, "context") and context.context:
            context.context.close()
        if hasattr(context, "browser") and context.browser:
            context.browser.close()
        if hasattr(context, "playwright") and context.playwright:
            context.playwright.stop()


def after_all(context):
    BrowserManager.close_browser()
    logger.info("=== Test Run Finished ===")
