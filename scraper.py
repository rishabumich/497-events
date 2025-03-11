import crawl4ai
import asyncio
import nest_asyncio
from playwright.async_api import async_playwright
from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig, CacheMode


nest_asyncio.apply()


async def test_browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://example.com')
        print(f'Title: {await page.title()}')
        await browser.close()

asyncio.run(test_browser())


async def simple_crawl():
    crawler_run_config = CrawlerRunConfig( cache_mode=CacheMode.BYPASS)
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com",
            config=crawler_run_config
        )
        print(result.markdown.raw_markdown[:500000].replace("\n", " -- "))  # Print the first 500 characters

asyncio.run(simple_crawl())