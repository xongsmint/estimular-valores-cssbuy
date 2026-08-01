# launches/manages playwright browser context
from playwright.async_api import async_playwright

async def create_browser():
    """
    **Starting browser**:
    ```
    p, browser = await create_browser()
    ```
    **Fully closing browser**:
    ```
    await browser.close()
    await p.stop()
    ```
    """
    p = await async_playwright().start()
    browser = await p.chromium.launch(
        headless=False,
        channel="chrome",
        args=["--disable-blink-features=AutomationControlled"],
    )
    return p, browser
