from playwright.sync_api import Page, expect, Locator
import allure


def _resolve_element(
    page: Page,
    *,
    locator: str = None,
    role: str = None,
    name: str = None,
    level: int = None,
    label: str = None,
    text: str = None,
    exact: bool = True,
    index: int = 0,
) -> Locator:
    """
    Resolve a Playwright Locator using:
      - locator (CSS/XPath)
      - get_by_role(role, name, level)
      - get_by_label(label)
      - get_by_text(text, excat)

    Parameters:
        page     : Playwright Page
        locator  : CSS or XPath selector
        role     : ARIA role (used with name)
        name     : Accessible name (used with role)
        lavel    : heading level h1,h2,h3..
        label    : Label text
        text     : Inner text (with exact match toggle)
        exact    : Whether get_by_text matches exactly (default=True)
        index    : Index of element if multiple matches
    """
    if locator:
        element = page.locator(locator)
    elif role:
        if level is not None:
            element = page.get_by_role(role, name=name, level=level)
        else:
            element = page.get_by_role(role, name=name)
    elif label:
        element = page.get_by_label(label)
    elif text:
        element = page.get_by_text(text, exact=exact)
    else:
        raise ValueError("Must provide one of: locator, role+name, label, or text.")

    return element.nth(index)


def click(page: Page, **kwargs) -> None:
    """Click an element."""
    try:
        locator = _resolve_element(page, **kwargs)
        locator.click()  # Playwright waits internally for clickable
    except Exception as e:
        raise RuntimeError(f"Failed to click element with args={kwargs}") from e


def get_inner_text(page: Page, **kwargs) -> str:
    """Return inner text of an element after Playwright default wait."""
    try:
        locator = _resolve_element(page, **kwargs)
        return locator.inner_text().strip()
    except Exception as e:
        raise RuntimeError(f"Failed to get inner text for args={kwargs}") from e


def get_element_by_text(
    page: Page, text: str, *, index: int = 0, exact: bool = True
) -> Locator:
    """Return element locator by visible text."""
    return _resolve_element(page, text=text, exact=exact, index=index)


def fill_input(page: Page, value: str, **kwargs) -> None:
    """Fill input element after Playwright default wait."""
    try:
        locator = _resolve_element(page, **kwargs)
        locator.fill(value)
    except Exception as e:
        raise RuntimeError(
            f"Failed to fill input for args={kwargs} with value='{value}'"
        ) from e


@allure.step("Expect element to be visible")
def to_be_visible(page: Page, **kwargs) -> None:
    """Assert element is visible after Playwright default wait."""
    try:
        locator = _resolve_element(page, **kwargs)
    except ValueError as e:
        raise  # argument error, fail immediately

    try:
        expect(locator).to_be_visible()  # waits internally
    except AssertionError as e:
        raise AssertionError(
            f"Element not visible after default Playwright timeout for args={kwargs}"
        ) from e


@allure.step("Expect element to have exact text: {expected_text}")
def expect_to_have_text(page: Page, expected_text: str, **kwargs) -> None:
    """Assert element has expected text after Playwright default wait."""
    try:
        locator = _resolve_element(page, **kwargs)
    except ValueError as e:
        raise

    try:
        expect(locator).to_have_text(expected_text)
    except AssertionError as e:
        raise AssertionError(
            f"Text mismatch for args={kwargs}. Expected: '{expected_text}'"
        ) from e


@allure.step("Expect element to contain text: {expected_text}")
def expect_to_contain_text(page: Page, expected_text: str, **kwargs) -> None:
    """Assert element contains expected text after Playwright default wait."""
    try:
        locator = _resolve_element(page, **kwargs)
    except ValueError as e:
        raise

    try:
        expect(locator).to_contain_text(expected_text)
    except AssertionError as e:
        raise AssertionError(
            f"Text containment failed for args={kwargs}. Expected to contain: '{expected_text}'"
        ) from e


def file_upload(page: Page, file_path: str, locator: str = "a#FILE") -> None:
    """
    Upload a file using a file chooser.

    Parameters:
        page      : Playwright Page
        file_path : Path to the file to upload
        locator   : Locator for the element that triggers file chooser (default: "a#FILE")
    """
    try:
        loc = _resolve_element(page, locator=locator)
        expect(loc).to_be_visible()
        with page.expect_file_chooser() as fc_info:
            loc.click()
        fc_info.value.set_files(file_path)
    except AssertionError as e:
        raise AssertionError(
            f"File upload failed: locator='{locator}' not visible"
        ) from e
    except Exception as e:
        raise RuntimeError(
            f"File upload failed for locator='{locator}' with file='{file_path}'"
        ) from e
