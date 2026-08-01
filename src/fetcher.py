# navigates + extracts the rate (network or DOM strategy)
from .browser import create_browser
from .config import cssbuy_cost_calculator_url
import asyncio

async def simulate_cost():
    p, browser = await create_browser()
    page = await browser.new_page()
    await page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    """)

    try:
        await page.goto(cssbuy_cost_calculator_url, timeout=10_000, wait_until="load")
        await page.wait_for_selector(".left_word", timeout=15_000)

        await asyncio.sleep(60 * 2)
    except Exception as e:
        print(f"Handled expected failure: {type(e).__name__}: {e}")
    finally:
        await browser.close()
        await p.stop()
        print("Browser closed cleanly regardless of success/failure")

    await browser.close()
    await p.stop()

