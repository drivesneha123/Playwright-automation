from playwright.sync_api import sync_playwright
import os


class BrowserManager:
    _playwright = None
    _browser = None

    @classmethod
    def launch_browser(cls, browser_name=None, headless=None):
        """
        Start Playwright and launch the desired browser.
        Supports: chromium, firefox, webkit.
        """
        if browser_name is None:
            browser_name = os.getenv("BROWSER", "chromium")

        if headless is None:
            headless = os.getenv("HEADLESS", "false").lower() == "true"

        cls._playwright = sync_playwright().start()

        if browser_name == "chromium":
            cls._browser = cls._playwright.chromium.launch(headless=headless)
        elif browser_name == "firefox":
            cls._browser = cls._playwright.firefox.launch(headless=headless)
        elif browser_name == "webkit":
            cls._browser = cls._playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        print(f"[BrowserManager] Launched {browser_name} (headless={headless})")
        return cls._browser

    @classmethod
    def close_browser(cls):
        """
        Cleanly close browser and stop Playwright.
        """
        if cls._browser:
            cls._browser.close()
        if cls._playwright:
            cls._playwright.stop()
        print("[BrowserManager] Browser and Playwright closed.")
