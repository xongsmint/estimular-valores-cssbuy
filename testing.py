from playwright.async_api import async_playwright
import time
import asyncio

async def get_execution_time(func, *args, **kwargs):
    start_time = time.perf_counter()
    await func(*args, **kwargs)
    end_time = time.perf_counter()
    return float(f"{(end_time - start_time):.4f}")

async def get_page_title(url: str): # ~2s execution time
                                    # part1: basic - open browser, go to page, close it
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(url)

        title = await page.title()
        print(f"Title: {title}")

        await browser.close()

async def get_user_repos(user: str): # ~2s execution time
                                     # part2: reading content from the dom
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(f"https://github.com/{user}", wait_until="domcontentloaded")
        repos = page.locator(".repo")
        repos = await repos.all_inner_texts()
        return repos

repos = asyncio.run(get_user_repos("xongsmint"))
print(repos)